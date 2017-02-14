#!/usr/bin/env python
from __future__ import division, print_function
import sys
import random, math, copy

sys.path.insert(0, '..')
sys.path.append('.')

from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)

from tutoring.models import Tutoring, Week3, Week4, Week5, Week6, Week7, Week8, Week9
from constants import TUTORING_DAY_CHOICES, TUTORING_HOUR_CHOICES

TUTORING_START = 10  # 10AM
TUTORING_END = 16  # 1 hr before 5pm

weeks = [
        Week3,
        Week4,
        Week5,
        Week6,
        Week7,
        Week8,
        Week9,
]

tutor_hours = {}

for week in weeks:
    for tutor_week_hours in week.objects.all():
        tutor = str(tutor_week_hours.profile())
        if tutor not in tutor_hours:
            tutor_hours[tutor] = 0
        tutor_hours[tutor] += tutor_week_hours.hours

for tutor, tutor_hours in sorted(list(tutor_hours.items()), key=lambda x: x[1], reverse=True):
    print("%s: %d" % (tutor, tutor_hours))


