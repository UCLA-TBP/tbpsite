#!/usr/bin/env python
from __future__ import division, print_function
import sys
import random, math, copy

sys.path.insert(0, '..')

from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)

from tutoring.models import Tutoring
from constants import TUTORING_DAY_CHOICES, TUTORING_HOUR_CHOICES
from main.models import Officer

MAX_TUTORS_PER_HOUR = 5
MIN_TUTORS_PER_HOUR = 2  # Want this
ENFORCED_MIN_TUTORS_PER_HOUR = 1  # Enforce this

TUTORING_START = 10  # 10AM
TUTORING_END = 16  # 1 hr before 5pm

OFFICERS_1_HOUR = True

tutoringHours = {}
for d in TUTORING_DAY_CHOICES:
    for h in TUTORING_HOUR_CHOICES:
        tutoringHours[( int(d[0]), int(h[0]) + TUTORING_START )] = []

# Add all 'frozen' tutors to schedule
tutoringObjs = []
allTutors = []
for t in Tutoring.current.all():
    allTutors.append(t)
    allTutors.append(t)
    if not t.hidden:
        if t.frozen:
            tutoringHours[( int(t.day_1), int(t.hour_1) + TUTORING_START )].append(t)
            tutoringHours[( int(t.day_2), int(t.hour_2) + TUTORING_START )].append(t)
        else:
            tutoringObjs.append(t)

officers = set()
for position in Officer.objects.all():
    for officer in position.profile.all():
        officers.add(officer)


def print_tutoring_hours_status(tutoringHours, enforce=False):
    min_satisfied = True
    max_satisfied = True
    total_assigned_hours = 0
    for slot in sorted(tutoringHours):
        assignees = tutoringHours[slot]
        printStr = ""
        for c in TUTORING_DAY_CHOICES:
            if int(c[0]) == slot[0]:
                printStr += c[1] + " at "
                break
        time = slot[1] % 12
        if not time:
            time = 12
        printStr += str(time) + ('AM' if slot[1] < 12 else 'PM') + ': '
        printStr += ', '.join(map(str, assignees))
        print(printStr)

        total_assigned_hours += len(assignees)

        if len(assignees) < ENFORCED_MIN_TUTORS_PER_HOUR:
            print ("*** The time slot above does not satisfy the minimum %d tutors per hour" % ENFORCED_MIN_TUTORS_PER_HOUR)
            min_satisfied = False

        if len(assignees) > MAX_TUTORS_PER_HOUR:
            max_satisfied = False
            #if len( assignees ) < ENFORCED_MIN_TUTORS_PER_HOUR:
            #    print "*** The time slot above does not satisfy the minimum %d tutors per hour" % ENFORCED_MIN_TUTORS_PER_HOUR
            #    minSatisfied = False

    print ('There are', len(Tutoring.current.all()), 'tutoring objects')
    print ('Total %d tutoring hours per week' % total_assigned_hours)

    if enforce:
        all_assigned = total_assigned_hours / len(Tutoring.current.all()) == 2

        print ('Minimum satisfied:', min_satisfied)
        print ('Maximum satisfied:', max_satisfied)
        print ('Everyone assigned:', all_assigned)

        if not all_assigned:
            tutors = []
            for tutor in Tutoring.current.all():
                tutors.append(tutor)
                tutors.append(tutor)

            assert len(allTutors) == len(Tutoring.current.all()) * 2

            for time, assignees in tutoringHours.iteritems():
                for assignee in assignees:
                    tutors.remove(assignee)

            print (tutors)

        assert min_satisfied and max_satisfied and all_assigned


def average(x):
    return sum(x)/len(x)


# class to hold times in a nice format
class TutoringTimes:
    def __init__(self, tutors, dayRange=(0, 5), hourRange=(10,17)):
        self.tutorTimes = {tutor: random.randint(0, len(tutor.preferences(two_hour=True)) - 1) for tutor in tutors}
        self.dayRange = dayRange
        self.hourRange = hourRange

        intervalsCovered = sum(map(
            lambda x: average(map(
                lambda y: sorted(y[1])[-1] - sorted(y[1])[0], x.preferences(two_hour=True)
            )), self.tutorTimes.keys()
        ))

        self.idealPerInterval = intervalsCovered / len(self.intervals())


    def __str__(self):
        intervals = self.intervals()
        for time, tutors in intervals.iteritems():
            intervals[time] = map(str, tutors)
        return str(intervals)

    def intervals(self):
        intervals = {(day, hour) : [] for hour in range(*self.hourRange) for day in range(*self.dayRange)}
        for tutor, selection in self.tutorTimes.iteritems():
            day, hours = tutor.preferences(two_hour=True)[selection]
            if OFFICERS_1_HOUR and tutor.profile in officers:
                intervals[(day, hours[0])].append(tutor)
            else:
                for hour in hours:
                    intervals[(day, hour)].append(tutor)

        return intervals

    def cost(self):

        intervals = self.intervals()

        cost = 0

        for _, selection in self.tutorTimes.iteritems():
            # covers cost of selecting 2nd or 3rd tutoring choices
            cost += 40 * (selection**2)

        for _, tutors in intervals.iteritems():
            # covers cost of having too full or too empty tutoring times
            cost += 10 * (len(tutors) - self.idealPerInterval) ** 4
            if len(tutors) == 0:
                cost += 100000
            elif len(tutors) == 1:
                cost += 10000

        return cost

    def changeRandomTutor(self):
        selectedTutor = self.tutorTimes.keys()[random.randint(0, len(self.tutorTimes) - 1)]
        self.tutorTimes[selectedTutor] = random.randint(0, len(selectedTutor.preferences(two_hour=True)) - 1)

# function that will generate optimized schedule
def annealingoptimize(tutoringTimes, T=100000, cool=0.95, step=1):
    while T > 0.1:
        # Create a new list with one of the values changed
        tutoringTimesNew = copy.deepcopy(tutoringTimes)
        tutoringTimesNew.changeRandomTutor()


        # Calculate the current cost and the new cost
        ea = tutoringTimes.cost()
        eb = tutoringTimesNew.cost()
        p = pow(math.e, (-eb - ea) / T)

        # Is it better, or does it make the probability
        # cutoff?
        if eb < ea or random.random() < p:
            tutoringTimes = tutoringTimesNew

        # Decrease the temperature
        T = T * cool
    return tutoringTimes

def best_annealing_optimize(tutoringTimes, generation_times=10, T=100000, cool=0.95, step=1):
    best_tutoringTimes = None
    for _ in range(generation_times):
        new_tutoringTimes = annealingoptimize(tutoringTimes, T, cool, step)
        if best_tutoringTimes==None or best_tutoringTimes.cost() > new_tutoringTimes.cost():
            best_tutoringTimes = new_tutoringTimes
    return best_tutoringTimes


tutoringTimes = TutoringTimes(tutoringObjs, dayRange=(0,5), hourRange=(10,17))
tutoringHours = best_annealing_optimize(tutoringTimes).intervals()

# Enforce min and max per hour
print_tutoring_hours_status(tutoringHours, enforce=False)

# Validate assigned hours with preferences
for time, assignees in tutoringHours.items():
    for assignee in assignees:
        if assignee.frozen:
            assert (time[0] == int(assignee.day_1)
                    and time[1] == int(assignee.hour_1) + TUTORING_START) or \
                   (time[0] == int(assignee.day_2)
                    and time[1] == int(assignee.hour_2) + TUTORING_START)
        else:
            assert (time in assignee.preferences(two_hour=False) or
                    time in [(t[0], t[1] + 1) for t in assignee.preferences(two_hour=False)])

# Commit
for time, assignees in sorted(tutoringHours.iteritems()):
    for assignee in assignees:
        if assignee.profile in officers:
            assignee.day_1 = str(time[0])
            assignee.hour_1 = str(time[1] - TUTORING_START)
            assignee.day_2 = str(time[0])
            assignee.hour_2 = str(time[1] - TUTORING_START)
        elif allTutors.count(assignee) == 2: # the strange way we check first or second hour
            allTutors.remove(assignee)
            assignee.day_1 = str(time[0])
            assignee.hour_1 = str(time[1] - TUTORING_START)
        else:
            assignee.day_2 = str(time[0])
            assignee.hour_2 = str(time[1] - TUTORING_START)

        assignee.save()
