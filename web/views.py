import operator
import re

from django.shortcuts import redirect

from common import MyTemplateView, render
from event.models import Event
from main.models import Candidate, Faculty, Officer
from tutoring.models import Feedback

about = MyTemplateView.as_view(template_name='about.html')
awards = MyTemplateView.as_view(template_name='awards.html')
candidates = MyTemplateView.as_view(template_name='candidates.html')
contact = MyTemplateView.as_view(template_name='contact.html')
emcc = MyTemplateView.as_view(template_name='emcc.html')
fe = MyTemplateView.as_view(template_name='fe.html')
home = MyTemplateView.as_view(template_name='home.html', 
        additional={'upcomingEvents': sorted(Event.objects.filter(dropdown=True), 
                key=operator.attrgetter('start'))})
programs = MyTemplateView.as_view(template_name='programs.html')
requirements = MyTemplateView.as_view(template_name='requirements.html')
tutoring = MyTemplateView.as_view(template_name='tutoring.html')

def faculty(request):
    faculty = Faculty.objects.all()
    facultyByDept = {}
    for f in faculty:
        facultyByDept.setdefault(str(f.get_dept_display()), []).append(
                (f.name, f.chapter, f.graduation, f.link))
    facultyByDept['Advisors'] = [
            ('William R. Goodin', 'CA E', "'75 (Chief Advisor)", ''),
            ('Stacey Ross', 'CA K', "'06 (District 16 Director)", ''),
            ('Neal Bussett', 'CA X', "'09 (District 16 Director)", ''),
            ('Jason Corl', 'CA Q', "'06 (District 16 Director)", ''),
            ('Scott Eckersall', 'CA I', "'96 (District 16 Director)", '')
            ]
    facultyByDept = [(dept, facultyByDept[dept]) for dept in sorted(facultyByDept)]
    return render(request, 'faculty.html', {
            'faculty' : facultyByDept,
            'facultyAdvisor' : 'Ann R. Karagozian'
        })

def feedback(request):
    if request.method == "POST" and 'comment' in request.POST:
        Feedback(comment=request.POST.get('comment')).save()
    return redirect('main.views.tutoring')

def officers(request):
    positionRe = re.compile( r'Club Liaison (\([^)]*\))' )
    positions = []
    liaisons = []
    for position in Officer.objects.all():
        match = positionRe.match( position.position )
        if match:
            for officer in position.profile.all():
                liaisons.append(' '.join([str(officer), match.group(1)]))
        else:
            positions.append( ( position.position, [ str( officer ) 
                for officer in position.profile.all() ] ) )

    positions.append( ( 'Faculty Advisor', [ 'Bill Goodin' ] ) )
    positions.append( ( 'Club Liaison', liaisons ) )

    return render(request, 'officers.html', {
            'term' : 'Summer - Fall 2013',
            'positions' : positions } )
