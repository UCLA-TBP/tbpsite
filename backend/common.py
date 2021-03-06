"""
This module contains utility functions that are used by multiple applications.
"""

from django.shortcuts import render as django_render
from django.views.generic.base import TemplateView

from event.models import Event
from main.models import Settings, HousePoints, Link


class MyTemplateView(TemplateView):

    additional = {}

    def get(self, request, *args, **kwargs):
        context = {'user': self.request.user, 'next': self.request.path,  'events': Event.objects.filter(dropdown=True , term=Settings.objects.term()),
                   'houses': HousePoints.current.all(), 'eligibility_list': Settings.objects.get_eligibility_list().url}
        context.update(self.additional)
        candidatePacketURLs = Link.objects.filter(name='candidate_packet_url')
        if len(candidatePacketURLs):
            context['candidatePacketURL'] = candidatePacketURLs[0].url
        orientationPresentations = Link.objects.filter(name='orientation_presentation')
        if len(orientationPresentations):
            context['orientationPresentationURL'] = orientationPresentations[0].url
        return self.render_to_response(context)


def render(request, template_name, additional=None):
    dictionary = {'user': request.user, 'next': request.path, 'events': Event.objects.filter(dropdown=True, term = Settings.objects.term()),
                  'houses': HousePoints.current.all(), 'eligibility_list': Settings.objects.get_eligibility_list().url}
    if additional is not None:
        dictionary.update(additional)

    candidatePacketURLs = Link.objects.filter(name='candidate_packet_url')
    if len(candidatePacketURLs):
        dictionary['candidatePacketURL'] = candidatePacketURLs[0].url
    orientationPresentations = Link.objects.filter(name='orientation_presentation')
    if len(orientationPresentations):
        dictionary['orientationPresentationURL'] = orientationPresentations[0].url
    return django_render(request, template_name, dictionary)
