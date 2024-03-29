import datetime
import re

from common import MyTemplateView
from event.models import Event
from main.models import Faculty, Officer, Settings, Link

about = MyTemplateView.as_view(template_name='about.html')
awards = MyTemplateView.as_view(template_name='awards.html')
candidates = MyTemplateView.as_view(template_name='candidates.html')
contact = MyTemplateView.as_view(template_name='contact.html')
emcc = MyTemplateView.as_view(template_name='emcc.html')
fe = MyTemplateView.as_view(template_name='fe.html')
home = MyTemplateView.as_view(template_name='home.html',
                              additional={'upcoming_events': [event for event in Event.objects.filter(
                                  dropdown=True, end__gt=datetime.datetime.today) if event.event_type != Event.SOCIAL],
                                  'display': Settings.objects.display_tutoring()})
programs = MyTemplateView.as_view(template_name='programs.html')
tutoring = MyTemplateView.as_view(template_name='tutoring.html')
sponsor = MyTemplateView.as_view(template_name='sponsor.html')
donate = MyTemplateView.as_view(template_name='donate.html')
room_calendar = MyTemplateView.as_view(template_name='calendar.html')

def get_faculty_by_dept():
    faculty = Faculty.objects.all()
    faculty_by_dept = {}
    for f in faculty:
        faculty_by_dept.setdefault(str(f.get_dept_display()), []).append((f.name, f.chapter, f.graduation, f.link))
    faculty_by_dept['Advisors'] = [
        ('Neal Bussett', 'CA X', "'09 (District 16 Director)", ''),
        ('Carissa Eisler', 'CA E', "'10 (Faculty Advisor)", ''),
        ('William R. Goodin', 'CA E', "'75 (Chief Advisor)", ''),
        ('Ann R. Karagozian', 'CA E', "'78 ", ''),
        ('Aaron Meyer', 'CA E', "'09 (Faculty Advisor)", ''),
        ('Sam Rokni', 'CA C', "'05 (District 16 Director)", '')
    ]
    return [(dept, sorted(faculty_by_dept[dept], key=lambda x: x[0].rsplit(None, 1)[-1])) for dept in sorted(faculty_by_dept)]

def get_officers():
    position_re = re.compile(r'Club Liaison (\([^)]*\))')
    positions = []
    liaisons = []
    liaison_alias = ''

    for position in Officer.objects.all():
        liaison_alias = position.mail_alias
        match = position_re.match(position.position)
        if match:
            for officer in position.profile.all():
                liaisons.append(' '.join([str(officer), match.group(1)]))
        else:
            positions.append((position.position, position.mail_alias, [str(officer) for officer in position.profile.all()]))

    # positions.append(('Faculty Advisor', None, ['Bill Goodin']))
    return positions

faculty = MyTemplateView.as_view(template_name='faculty.html',
                                 additional={'faculty': get_faculty_by_dept, 'facultyAdvisor': 'Ann R. Karagozian'})
officers = MyTemplateView.as_view(template_name='officers.html',
                                  additional={'term': Settings.objects.term(), 'positions': get_officers})
requirements = MyTemplateView.as_view(template_name='requirements.html',
                                      additional={})
