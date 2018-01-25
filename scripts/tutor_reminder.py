#!/usr/bin/env python
from __future__ import division, print_function
import sys

sys.path.insert(0, '..')
sys.path.append('.')

import smtplib

from tbpsite import settings
from django.core.management import setup_environ

setup_environ(settings)

from main.models import Settings, Profile
from tutoring.models import Tutoring, Week3, Week4, Week5, Week6, Week7, Week8, Week9

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
week_tutor_hours = {}
c_term = Settings.objects.term()

tutoring_weeks_completed = c_term.get_week() - 2
c_week = weeks[tutoring_weeks_completed - 1]
expected_hours = tutoring_weeks_completed * 2 
minimum_hours = expected_hours / 2

for week in weeks:
    for tutor_week_hours in week.objects.all():
        tutor = tutor_week_hours.profile()
        if tutor not in tutor_hours:
            tutor_hours[tutor] = 0
        tutor_hours[tutor] += tutor_week_hours.hours

long_bad_tutors = {}
for tutor, hours in tutor_hours.items():
    if Tutoring.current.get(profile=tutor).hidden:
        continue
    if not tutor.position == Profile.CANDIDATE:
        if hours < minimum_hours:
            long_bad_tutors[tutor] = minimum_hours - hours
    elif hours < expected_hours:
        long_bad_tutors[tutor] = expected_hours - hours

for tutor_week_hours in c_week.objects.all():
    tutor = tutor_week_hours.profile()
    if tutor not in week_tutor_hours:
        week_tutor_hours[tutor] = 0
    week_tutor_hours[tutor] += int(tutor_week_hours.hours)

tutors_0_hr = set()
tutors_1_hr = set()
for tutor, hours in week_tutor_hours.items():
    if Tutoring.current.get(profile=tutor).hidden:
        continue
    if hours == 0:
        tutors_0_hr.add(tutor)
    elif hours == 1 and tutor.position == Profile.CANDIDATE:
        tutors_1_hr.add(tutor)

last_name = lambda x: x.user.last_name

bad_tutors = sorted(list(tutors_0_hr | tutors_1_hr | set(long_bad_tutors.keys())), key = last_name)
bad_tutors_week = sorted(list(tutors_0_hr | tutors_1_hr), key = last_name)
tutors_0_hr = sorted(list(tutors_0_hr), key = last_name)
tutors_1_hr = sorted(list(tutors_1_hr), key = last_name)
    
from_addr = 'tutoring@tbp.seas.ucla.edu'
to_addrs = []
#to_addrs = ['tutoring@tbp.seas.ucla.edu']
#cc = []
#cc = ['webmaster@tbp.seas.ucla.edu', 'officers@tbp.seas.ucla.edu']
cc = ['tutoring@tbp.seas.ucla.edu', 'mark@marktai.com', 'oozgur217@gmail.com']
bcc = []
for tutor in bad_tutors:
    bcc.append(tutor.user.email)

message_subject = "[TBP] Week %d Missing Tutoring Hours" % c_term.get_week()
message_text = \
"""Hi Tutors,

The following is a list of people who have missed tutoring hours. If you are on this list, you must contact the tutoring chairs (tutoring@tbp.seas.ucla.edu) to make up your hours. 
If you have contacted us before about changing your hours, or you believe there may be a mistake in the provided information, please let us know.

Please take a look at the schedule (https://tbp.seas.ucla.edu/schedule/), pick a make-up time slot to attend and send an email back to us with your choice.

Please remember to sign in and out at the appropriate times as well.

If you did sign in but the system did not record it, please respond as well and if any officer saw you in the tutoring room, please give us his/her name as well. 

Missing Hours in Week %d
%s

Missing Hours in %s
%s

Best, 
Omar""" % (c_term.get_week(), '\n'.join(map(str, bad_tutors_week)), c_term, '\n'.join(['%s (%d hours missing)' % (str(tutor), missing_hours) for tutor, missing_hours in sorted(list(long_bad_tutors.items()), key=lambda x: (-x[1], last_name(x[0])))]))

message = (
          "From: %s\r\n" % from_addr
        + "To: %s\r\n" % ",".join(to_addrs)
        + "CC: %s\r\n" % ",".join(cc)
        + "Subject: %s\r\n" % message_subject
        + "\r\n" 
        + message_text
)

recipients = to_addrs + cc + bcc
server = smtplib.SMTP('tbp.seas.ucla.edu')
server.login(from_addr, settings.EMAIL_PASSWORD)
#server.set_debuglevel(1)
#server.sendmail(from_addr, recipients, message)

print("sending to %s" % repr(bad_tutors))
print(message)
server.quit()

