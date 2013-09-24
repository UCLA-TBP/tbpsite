import re

from main.models import Settings
from tutoring.models import Tutoring, Class 
from common import render

number = re.compile(r'\d+')
numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen']


def schedule(request):
    term = Settings.objects.term()
    tutoring = Tutoring.objects.filter(term=term)
    tutors = []
    for hour, hour_name in Tutoring.HOUR_CHOICES:
        tutors_for_hour = []
        for day, day_name in Tutoring.DAY_CHOICES:
            if Settings.objects.display_tutoring() or (request.user.is_authenticated and request.user.is_staff):
                tutors_for_hour.append(list(tutoring.filter(hour_1=hour, day_1=day)) + list(tutoring.filter(hour_2=hour, day_2=day)))
            else:
                tutors_for_hour.append(None)
        tutors.append((hour_name, tutors_for_hour))

    classes = []
    for department, number in zip(Class.DEPT_CHOICES, numbers):
        department, _ = department
        classes.append(
            (department, [
                (cls.course_number, cls.department+cls.course_number)
                for cls in sorted(Class.objects.filter(department=department, display=True),
                                  key=lambda c: tuple(int(s) if s.isdigit() else s
                                                      for s in re.search(r'(\d+)([ABCD]?L?)?',
                                                                         c.course_number).groups()))
            ], 'collapse{}'.format(number)))
            
    return render(request, 'schedule.html', {'term': term, 'classes': classes, 'tutors': tutors})
