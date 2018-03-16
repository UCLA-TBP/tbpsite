#!/usr/bin/env python from __future__ import division, print_function
import sys
import random, math, copy
import pdb
import csv

sys.path.insert(0, '..')
sys.path.append('.')

from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)

from tutoring.models import Tutoring
from constants import TUTORING_DAY_CHOICES, TUTORING_HOUR_CHOICES
csvFileName = sys.argv[1]

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

days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}

subjects = set()

for ls in data.values():
  for item in ls:
    subject = item.split(' ')[0]
    if subject not in subjects:
      subjects.add(subject)

subjects = sorted(list(subjects))

def format_classes(classes_lst):
    formatted_classes_lst = [','.join([class_str.split(' ')[1] for class_str in classes_lst if subject in class_str]) for subject in subjects]
    return formatted_classes_lst

with open(csvFileName, 'wb') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Hour', 'Class'] + days.values())
    for hour in range(TUTORING_START, TUTORING_END + 1):
        classes = []
        for day in days:
            classes.append(format_classes(data[(day, hour)]))
        rows = zip(*classes)
        for index, row in enumerate(rows):
            writer.writerow([str(hour) if not index else '', subjects[index]] + list(row))
