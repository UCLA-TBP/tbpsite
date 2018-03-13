# TBP Site

The UCLA Tau Beta Pi website runs on the Django framework.  It uses server side rendering and minimal frontend JS.


## Contributing
Grep is an extremely useful tool to navigate the folders
  - `grep -R "$STRING_TO_FIND" $FOLDER` will find all instances of `$STRING_TO_FIND` in `$FOLDER`

### Frontend change
You will be modifying `tbpsite/templates` and `tbpsite/tbpsite/static`.  Use `grep` to find out which template file you want to modify specifically.

### Backend change
You will be probably be modifying models and views.  Use `grep` to find where the specific model is defined.
When creating a new object, please use `CapitalCamelCase`

### Creating a new script
You probably want to find a script that does something similar to what you're trying to already do and use that as an example.  

Make sure to include the following on the top to make it run
``` python
#! /usr/bin/python
import sys

sys.path.insert(0, '..')
sys.path.append('.')
```

## Folder Layout
```
.
├── cached_templates  # folder used for caching the tutoring schedule
├── Dockerfile  # config file for Docker image setup
├── event
│   ├── admin.py    # config file for admin page (/admin)
│   ├── forms.py    # configures forms for user input
│   ├── migrations  # folder for generated Django migrations (sql schema changes)
│   ├── models.py   # configures event models and behaviors
│   └── views.py    # configures views (HTML and HTTP endpoints) for events
├── main
│   ├── admin.py    # config file for admin page
│   ├── forms.py    # configures forms for user input                    
│   ├── migrations  # folder for generated Django migrations (sql schema changes)
│   ├── models.py   # configures event models and behaviors
│   └── views.py    # configures views (HTML and HTTP endpoints) for main models of TBP
├── requirements.txt  # Python modules that the TBP site requires.  Is used in the Dockerfile
├── scripts
│   ├── add_ao_and_emcc.py          # adds Academic Outreach and EMCC officers to distinguished active members
│   ├── assign_tutoring.py          # assigns tutors to a tutoring time
│   ├── dumpTutoringToCsv.py        
│   ├── dumpTutoringToSheet.py      
│   ├── exportTutors.py
│   ├── find_bad_officers.py        # finds officers who haven't signed up for tutoring
│   ├── getMemberInfo.py    
│   ├── parse_foreign_csv.py
│   ├── submission_times.py
│   ├── tutor_reminder.py           # sends an email to bad tutors
│   └── updateSchedule.sh           # updates the tutoring schedule (creates new cached copy)
├── tbpsite    # global stuff
│   ├── settings.py   # global settings for the website
│   ├── static        # folder to insert css, img, and js files for the website (edit the website styling here)
│   └── urls.py       # global URL's for the website
├── templates  # folder for all HTML templates to be rendered by Django (edit the website layout here)
├── tutoring
│   ├── admin.py    # config file for admin page
│   ├── management  # contains scripts to manage tutoring (create cache copy of tutoring schedule)
│   ├── migrations  # folder for generated Django migrations (sql schema changes)
│   ├── models.py   # configures event models and behaviors
│   └── views.py    # configures views (HTML and HTTP endpoints) for tutoring
└── web
    └── views.py    # configures views for random pages
```
