#!/usr/bin/env python
from __future__ import division, print_function
import sys
import random, math, copy

sys.path.insert(0, '..')
sys.path.append('.')

from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)

from tutoring.models import Tutoring
from constants import TUTORING_DAY_CHOICES, TUTORING_HOUR_CHOICES


MAX_TUTORS_PER_HOUR = 5
MIN_TUTORS_PER_HOUR = 2  # Want this
ENFORCED_MIN_TUTORS_PER_HOUR = 1  # Enforce this

TUTORING_START = 10  # 10AM
TUTORING_END = 16  # 1 hr before 5pm

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


print(repr(tutoringHours))


