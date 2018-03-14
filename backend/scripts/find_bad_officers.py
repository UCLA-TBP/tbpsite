#! /usr//bin/python

from __future__ import division, print_function
import sys

sys.path.insert(0, '..')
sys.path.append('.')


from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)


from main.models import Officer, ActiveMember, Profile

officer_profiles = Officer.objects.all().values_list('profile', flat=True)

bad_officer_profile_ids = set(officer_profiles) - set(ActiveMember.current.all().values_list('profile', flat=True))

bad_officers = Profile.objects.filter(id__in=bad_officer_profile_ids)

for officer in sorted(map(str, bad_officers)):
    print(officer)


