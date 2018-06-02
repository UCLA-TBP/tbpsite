#!/usr/bin/env python from __future__ import division, print_function
import sys
import random, math, copy
import pdb

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


data = tutoringHours

toDay = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}

sortedData = sorted(data.items(), key=lambda x: (x[0][1], x[0][0]))

subjects = set()
for ls in data.values():
  for item in ls:
    subject = item.split(' ')[0]
    if subject not in subjects:
      subjects.add(subject)

currentTime = None
fields = {}
for item in sortedData:
  if item[0][1] != currentTime and currentTime:
    currentDay = 0
    print("Hour: {}".format(currentTime))
    for day in fields.items():
      print(toDay[day[0]])
      for subject in sorted(day[1].items(), key=lambda x: x[0]):
        print(subject[0] + ": " + ' '.join(subject[1]))
      print("")
    currentTime = item[0][1]
    fields = {}
  else:
    currentTime = item[0][1]
  fields[item[0][0]] = {}
  for subject in item[1]:
    if subject.split(' ')[0] not in fields[item[0][0]]:
      fields[item[0][0]][subject.split(' ')[0]] = [subject.split(' ')[1]]
    else:
      fields[item[0][0]][subject.split(' ')[0]].append(subject.split(' ')[1])
if fields:
  currentDay = 0
  print("Hour: {}".format(currentTime))
  for day in fields.items():
    print(toDay[day[0]])
    for subject in sorted(day[1].items(), key=lambda x: x[0]):
      print(subject[0] + ": " + ' '.join(sorted(subject[1])))
    print("")
  currentTime = item[0][1]
  fields = {}
