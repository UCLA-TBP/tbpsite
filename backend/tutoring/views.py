import itertools
import re
import datetime
import random, math, copy
import pdb
import csv

from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

from common import render
from main.models import Settings, Profile
from tutoring.models import Tutoring, ForeignTutoring, Class
from constants import TUTORING_HOUR_CHOICES, TUTORING_DAY_CHOICES
from django.template.loader import render_to_string
from collections import OrderedDict
import subprocess

number = re.compile(r'\d+')
numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen']


def get_classes():
    """
    :return:
    """
    classes = []
    for department, number in zip(Class.DEPT_CHOICES, numbers):
        department, _ = department
        courses = [(cls.course_number, cls.department+cls.course_number)
                   for cls in sorted((c for c in Class.objects.filter(department=department, display=True)
                       if any(filter(lambda x: x.active(), c.profile_set.all()))),
                                     key=lambda c: tuple(int(s) if s.isdigit() else s
                                                         for s in re.search(r'(\d+)([ABCD]?L?)?',
                                                                            c.course_number).groups()))]
        if courses:
            classes.append((department, courses, 'collapse{}'.format(number)))
    return classes


def get_tutors():
    """
    :return:
    """
    tutors = []
    for hour, hour_name in TUTORING_HOUR_CHOICES:
        tutors_for_hour = []
        tutoring_objs = [t for t in Tutoring.current.all()] + [t for t in ForeignTutoring.current.all()]
        for day, day_name in TUTORING_DAY_CHOICES:
            tutors_for_hour.append(
                sorted([t for t in tutoring_objs
                        if (not t.hidden) and ((t.hour_1 == hour and t.day_1 == day) or (t.hour_2 == hour and t.day_2 == day))],
                       key=lambda t: t.__unicode__()))
        tutors.append((hour_name, tutors_for_hour))
    return tutors


def schedule(request):
    """
    :param request:
    :return:
    """
    term = Settings.objects.term()
    should_display = request.user.is_staff or Settings.objects.display_tutoring()

    current_tutors = Tutoring.current.filter(
        is_tutoring=True,
        last_start__gte=datetime.datetime.now().date(),
    )

    tutor_profiles = Profile.current.filter(
        id__in=map(lambda x: x.profile.id, current_tutors),
    )
    current_classes_covered = set()
    for profile in tutor_profiles:
        current_classes_covered |= set(profile.classes.all())

    tutor_profiles = sorted(list(tutor_profiles), key=str)
    current_classes_covered = sorted(
        list(current_classes_covered),
        key=lambda x: (x.department, int(''.join([s for s in x.course_number if s.isdigit()]))), #sorts by department, then by number of course_number
    )

    department_classes = {}
    for cls in current_classes_covered:
        department_classes.setdefault(cls.department, [])
        department_classes[cls.department].append(cls)

    display_current_tutors = should_display and (tutor_profiles or current_classes_covered)

    current_tutor_list_string = ', '.join(map(str, current_tutors))
    for dep, cls_list in department_classes.iteritems():
        department_classes[dep] = ', '.join(map(lambda x: str(x.course_number), cls_list))
    department_classes = sorted(list(department_classes.iteritems()), key=lambda x: x[0]) # to sort by department


    if not should_display:
        return render(
            request,
            'schedule.html',
            {
                'schedule_block': 'no_display_schedule_snippet.html',
                'term': term,
                #'classes': get_classes(),
                'classes': [],
                #'tutors': get_tutors(),
                'tutors': [],
                'display': should_display,
                'display_current_tutors': display_current_tutors,
                'current_tutors_string': current_tutor_list_string,
                #'department_classes': department_classes,
                'department_classes': [],
            },
        )


    # the cached template always displays the schedule
    try:
        return render(
            request,
            'schedule.html',
            {
                'schedule_block': 'cached_schedule_snippet.html',
                'term': term,
                'display': should_display,
                'display_current_tutors': display_current_tutors,
                'current_tutors_string': current_tutor_list_string,
                'department_classes': department_classes,
            },
        )
    except:
        # save cache
        tutors = get_tutors()
        classes = get_classes()
        content = render_to_string('schedule_snippet.html', {'tutors':tutors,'classes':classes})
        with open('cached_templates/cached_schedule_snippet.html', 'w') as static_file:
            static_file.write(content)
        return render(
            request,
            'schedule.html',
            {
                'schedule_block': 'cached_schedule_snippet.html',
                'term': term,
                'display': should_display,
                'display_current_tutors': display_current_tutors,
                'current_tutors_string': current_tutor_list_string,
                'department_classes': department_classes,
            },
        )

@login_required(login_url='/login')
def update_schedule(request):
    """ updates the schedule by removing the cache and rerendering the page
    """
    subprocess.call(["rm", "-f", "cached_templates/cached_schedule_snippet.html"])
    return HttpResponseRedirect('/schedule/')

@login_required()
def classes(request):
    """
    :param request:
    :return:
    """
    term = Settings.objects.term()
    tutors = []
    for hour, hour_name in TUTORING_HOUR_CHOICES:
        tutors_for_hour = []
        tutoring_objs = [t for t in Tutoring.current.all()] + [t for t in ForeignTutoring.current.all()]
        for day, day_name in TUTORING_DAY_CHOICES:
            tutors_for_hour.append(
                sorted(t for t in tutoring_objs
                       if (t.hour_1 == hour and t.day_1 == day) or (t.hour_2 == hour and t.day_2 == day)) +
                sorted(itertools.chain.from_iterable(t.profile.classes.all() for t in tutoring_objs
                                                     if (t.hour_1 == hour and t.day_1 == day) or (t.hour_2 == hour and t.day_2 == day))))
        tutors.append((hour_name, tutors_for_hour))

    return render(request, 'classes.html', {'term': term, 'tutors': tutors})


@login_required()
def expanded_schedule(request):
    """
    :param request:
    :return:
    """
    term = Settings.objects.term()
    tutors = []
    for hour, hour_name in TUTORING_HOUR_CHOICES:
        tutors_for_hour = []
        for day, day_name in TUTORING_DAY_CHOICES:
            if Settings.objects.display_tutoring() or (request.user.is_authenticated and request.user.is_staff):
                tutors_for_hour.append(['{} {}'.format(1, tutor) for tutor in Tutoring.current.filter(best_hour=hour, best_day=day)] +
                                       ['{} {}'.format(1, tutor) for tutor in Tutoring.current.filter(best_hour=str(int(hour)-1), best_day=day)] +
                                       ['{} {}'.format(2, tutor) for tutor in Tutoring.current.filter(second_best_hour=hour, second_best_day=day)] +
                                       ['{} {}'.format(2, tutor) for tutor in Tutoring.current.filter(second_best_hour=str(int(hour)-1), second_best_day=day)] +
                                       ['{} {}'.format(3, tutor) for tutor in Tutoring.current.filter(third_best_hour=hour, third_best_day=day)] +
                                       ['{} {}'.format(3, tutor) for tutor in Tutoring.current.filter(third_best_hour=str(int(hour)-1), third_best_day=day)])
            else:
                tutors_for_hour.append(None)
        tutors.append((hour_name, tutors_for_hour))

    classes = []
    for department, number in zip(Class.DEPT_CHOICES, numbers):
        department, _ = department
        courses = [(cls.course_number, cls.department+cls.course_number)
                   for cls in sorted((c for c in Class.objects.filter(department=department, display=True)
                       if any(filter(lambda x: x.active(), c.profile_set.all()))),
                                     key=lambda c: tuple(int(s) if s.isdigit() else s
                                                         for s in re.search(r'(\d+)([ABCD]?L?)?',
                                                                            c.course_number).groups()))]
        if courses:
            classes.append((department, courses, 'collapse{}'.format(number)))

    return render(request, 'schedule.html', {'term': term, 'classes': classes, 'tutors': tutors,
                                             'display': request.user.is_staff or Settings.objects.display_tutoring()})
def feedback(request):
    return render(request, 'tutoring_feedback.html')

@login_required(login_url='/login')
def tutoring_logging(request):
    """
    :param request:
    :return:
    """
    c_term = Settings.objects.term()

    tutoring = None
    error = None
    isTutoring = False
    hours = 0
    classes = None
    confirm = False

    last_logged_in = None
    sign_out_time = None

    # tutoring = get_object_or_404(Tutoring, profile=request.user.profile, term=c_term)
    try:
        tutoring = Tutoring.objects.get(profile=request.user.profile, term=c_term)
    except Tutoring.DoesNotExist:
        # Quick patch to make the error nice while we add allowance of weeks 1 and 2.
        # TODO: Find out what the true problem is for this user. It can be any of:
        #   1. Week < 3
        #   2. Non-candidate (no peer teaching at all)
        #   3. Candidate who chose Academic Outreach
        # The error should be a diagnostic on one of these issues.
        error = "We apologize, but you cannot log your tutoring hours at this time. Please try again tomorrow."

    if tutoring:
        isTutoring = tutoring.is_tutoring

        td = (datetime.datetime.now() - tutoring.last_start).seconds
        hours = td // 3600
        if (td // 60) % 60 >= 45:
            hours += 1

        display_signout_screen = True

        if request.method == "POST":
            if 'sign_in' in request.POST and not isTutoring:
                display_signout_screen = False
                tutoring.is_tutoring = True
                isTutoring = True
                tutoring.last_start = datetime.datetime.now()
                hours = 0
                classes = Class.objects.filter(display=True)
                confirm = True

            elif 'sign_out' in request.POST:
                display_signout_screen = False
                last_logged_in = tutoring.last_start
                sign_out_time = datetime.datetime.now()
                h = hours
                tutees = int(request.POST['tutees'])
                makeup_t = int(request.POST['makeup_tutoring'])
                makeup_e = int(request.POST['makeup_event'])
                class_ids = request.POST.getlist('subjects')

                if (makeup_t + makeup_e) > hours:
                    error = ('Hmm please check your math. According to our records, you have tutored approximately {} '
                             'hours this session (we round up after 45 minutes), but you have indicated {} makeup hours.'.format(str(hours), str(makeup_t + makeup_e)))
                    display_signout_screen = True
                else:
                    tutoring.is_tutoring = False
                    isTutoring = False
                    week = c_term.get_week()
                    if makeup_e > 0:
                        h -= makeup_e # hours not logged!
                        send_mail('Make up Tutoring Hours!',
                                  'Hi! {} indicated they tutored {} hours to make up for an event. Please check this out! -- Tutoring Bot'.format(tutoring.profile, makeup_e),
                                  'tutoring@tbp.seas.ucla.edu', ['tutoring@tbp.seas.ucla.edu', 'board@tbp.seas.ucla.edu'], fail_silently=True)

                    if makeup_t > 0:
                        for i in range(3, week):
                            week_obj = getattr(tutoring, 'week_'+str(i))
                            while (not week_obj.complete()) and makeup_t > 0:
                                week_obj.hours += 1
                                h -= 1
                                makeup_t -= 1
                                week_obj.no_makeup = False
                            week_obj.save()
                    cur_week = getattr(tutoring, 'week_'+str(week))
                    cur_week.hours += h
                    cur_week.tutees += tutees
                    cur_week.save()
                    for s in class_ids:
                        s = int(s)
                        cur_week.classes.add(Class.objects.get(id=s))
                    confirm = True

        else:
            if tutoring.is_tutoring and tutoring.last_start.date() != datetime.datetime.now().date():  # midnight passed :P
                display_signout_screen = False
                error = 'You forgot to sign out of your last tutoring session. Please contact the tutoring chair at tutoring@tbp.seas.ucla.edu to have those hours logged'
                tutoring.is_tutoring = False

        if display_signout_screen:
            classes = Class.objects.filter(display=True)

        tutoring.save()

    return render(request, 'tutoring_logging.html', {'error': error, 'isTutoring': isTutoring, 'hours': hours, 'classes': classes, 'confirm': confirm,
                                                     'last_logged_in': last_logged_in,
                                                     'sign_out_time': sign_out_time})

def getTutoringCsv(request):
    # Manifest constants
    MAX_TUTORS_PER_HOUR = 5
    MIN_TUTORS_PER_HOUR = 2  # Want this
    ENFORCED_MIN_TUTORS_PER_HOUR = 1  # Enforce this

    TUTORING_START = 10  # 10AM
    TUTORING_END = 16  # 1 hr before 5pm

    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tutoring.csv"'
    tutoringHours = {}
    for d in TUTORING_DAY_CHOICES:
        for h in TUTORING_HOUR_CHOICES:
            tutoringHours[( int(d[0]), int(h[0]) + TUTORING_START )] = set()

    for t in Tutoring.current.all():
        if not t.hidden:
            tutoringHours[(int(t.day_1), int(t.hour_1) + 10)] |= set(map(lambda x: str(x), list(t.profile.classes.all())))
            tutoringHours[(int(t.day_2), int(t.hour_2) + 10)] |= set(map(lambda x: str(x), list(t.profile.classes.all())))

    for key in tutoringHours:
        tutoringHours[key] = list(tutoringHours[key])

    data = tutoringHours
    subjects = set()
    for ls in data.values():
      for item in ls:
        subject = item.split(' ')[0]
        if subject not in subjects:
          subjects.add(subject)

    subjects = sorted(list(subjects))

    # utility function
    def format_classes(classes_lst):
        class_map = OrderedDict()
        for class_str in sorted(classes_lst):
            department, class_num = class_str.split(' ')
            class_map.setdefault(department, [])
            class_map[department].append(class_num)
        hour_day_classes = ''
        for department, class_nums in class_map.items():
            hour_day_classes += "%s: %s\n" % (department, ','.join(class_nums))
        return hour_day_classes
    writer = csv.writer(response)
    writer.writerow(['Hour'] + days.values())
    for hour in range(TUTORING_START, TUTORING_END + 1):
        classes = []
        for day in days:
            classes.append(format_classes(data[(day, hour)]))
        writer.writerow([str(hour)] + classes)
    return response