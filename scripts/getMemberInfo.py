#!/usr/bin/python

#import dependencies
import sys
sys.path.insert(0, "..")
sys.path.append(".") 
from optparse import OptionParser
from django.core.management import setup_environ
from tbpsite import settings
setup_environ(settings)

#setup models
from main.models import Profile
from main.models import Term
from main.models import User

#parameters
parser = OptionParser()
parser.add_option("-b", "--begin_year", dest="b_year", help="year to start query")
parser.add_option("-e", "--end_year", dest="e_year", help="year to end query")
parser.add_option("-f", "--fall_term", dest="fterm", action="store_true")
parser.add_option("-s", "--spring_quarter", dest="sterm", action="store_true")

(options, args) = parser.parse_args()

if options.b_year==None or options.e_year==None:
    raise ValueError("No begin year or end year parameter given")

majors = ["Aerospace Engineering", "Bioengineering", "Chemical Engineering", "Civil Engineering", "Computer Science", "Computer Science and Engineering", "Electrical Engineering", "Materials Engineering", "Mechanical Engineering"]

queryParams = Term.objects.filter(pk__in=[13, 19, 16, 3])
people = Profile.objects.filter(initiation_term__in=queryParams)

print type(people[0].major)

#write CSV
import csv
with open("members_out.csv", "wb") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'email', 'major', 'initation_term', 'graduation_term'])
    for item in people:
        writer.writerow([item.user.first_name + " " + item.user.last_name, \
                         item.user.email, \
                         majors[int(item.major)], \
                         item.initiation_term, \
                         item.graduation_term])
