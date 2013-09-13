from django.conf.urls import patterns, include, url
import django

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home', name='home'),

    url(r'^requirements/$', 'web.views.requirements'),
    url(r'^programs/$', 'web.views.programs'),
    url(r'^emcc/$', 'web.views.emcc'),
    url(r'^fe/$', 'web.views.fe'),
    url(r'^about/$', 'web.views.about'),
    url(r'^awards/$', 'web.views.awards'),
    url(r'^officers/$', 'web.views.officers'),
    url(r'^faculty/$', 'web.views.faculty'),
    url(r'^tutoring/$', 'web.views.tutoring'),
    url(r'^feedback/$', 'web.views.feedback'),
    url(r'^contact/$', 'web.views.officers'),
    url(r'^eligibility_list/$', 'web.views.eligibility_list'),
    url(r'^candidates/$', 'web.views.candidates'),

    url(r'^tutoring_hours/$', 'main.views.tutoring_hours'),
    url(r'^tutoring_feedback/$', 'main.views.tutoring_feedback'),
    url(r'^schedule/$', 'tutoring.views.schedule'),
    url(r'^houses/$', 'main.views.houses'),

    url(r'^candidate_requirements/$', 'main.views.candidates'),
    url(r'^active_members/$', 'main.views.active_members'),
    url(r'^preferences/$', 'tutoring.views.preferences'),
    url(r'^downloads/$', 'main.views.downloads'),
    url(r'^spreadsheet/$', 'main.views.spreadsheet'),

    url(r'^logout/$', 'main.views.logout'),
    url(r'^login/$', 'main.views.login'),
    url(r'^profile/$', 'main.views.profile_view'),
    url(r'^edit/(?P<from_redirect>\w+?)$', 'main.views.edit'),
    url(r'^edit/$', 'main.views.edit'),
    url(r'^add/$', 'main.views.add'),
    url(r'^register/$', 'main.views.register'),

    url(r'^resume_pdf/$', 'main.views.resume_pdf'),
    url(r'^resume_word/$', 'main.views.resume_word'),
    url(r'^interview/$', 'main.views.interview'),

    # url(r'^events/', include('event.site.urls')),
    url(r'^events/$', 'event.views.events'),
    url(r'^events/(?P<url>\w+)/$', 'event.views.event'),
    url(r'^cb_race/$', 'event.views.event_redirect', 
        {'event_url': 'cb_race'}),
    url(r'^scholarship/$','event.views.event_redirect', 
        {'event_url': 'scholarship'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
