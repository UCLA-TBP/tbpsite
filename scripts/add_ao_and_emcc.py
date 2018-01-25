#! /usr//bin/python

from __future__ import division, print_function
import sys

sys.path.insert(0, '..')
sys.path.append('.')


from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)


from main.models import Officer, ActiveMember, Profile, Settings

ao = Profile.objects.filter(id__in = Officer.objects.filter(position='Academic Outreach').values_list('profile', flat=True))
for p in ao:
    if ActiveMember.objects.filter(profile=p, term=Settings.objects.term()).exists():
        continue
    ActiveMember(profile=p, term=Settings.objects.term(), requirement_choice=ActiveMember.ACAD_OUTREACH).save()
    print('Adding %s to AO' % p)

emcc = Profile.objects.filter(id__in = Officer.objects.filter(position='Education Outreach').values_list('profile', flat=True))
for p in emcc:
    if ActiveMember.objects.filter(profile=p, term=Settings.objects.term()).exists():
        continue
    ActiveMember(profile=p, term=Settings.objects.term(), requirement_choice=ActiveMember.EMCC).save()
    print('Adding %s to EMCC' % p)

