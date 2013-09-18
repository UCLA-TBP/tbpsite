from django.contrib import admin
from tutoring.models import *

def fill_hours(modeladmin, request, queryset):
    for member in queryset:
        member.hours = TUTORING_HOURS_PER_WEEK
        member.save()

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'comment') 
    def __init__(self, *args, **kwargs):
        super(FeedbackAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None,)

class ClassAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'display')
    list_editable = ('display',)

class TutoringAdmin(admin.ModelAdmin):
    fields = ('day_1', 'hour_1', 'day_2', 'hour_2')
    list_display = ('__unicode__', 'term', 'day_1', 'hour_1', 'day_2', 'hour_2')
    list_editable = ('day_1', 'hour_1', 'day_2', 'hour_2')
    actions = ('import_tutoring_times',)

    def import_tutoring_times(modeladmin, request, queryset):
        for tutoring in queryset:
            tutoring.day_1 = tutoring.day_2 = tutoring.best_day
            tutoring.hour_1 = tutoring.best_hour
            tutoring.hour_2 = str(int(tutoring.hour_1) + 1)
            tutoring.save()

class WeekAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'term', 'day_1', 'hour_1', 'day_2', 'hour_2', 'hours', 'tutees')
    list_editable = ('hours', 'tutees')
    actions = (fill_hours,)
    
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Tutoring, TutoringAdmin)
admin.site.register(Week3, WeekAdmin)
admin.site.register(Week4, WeekAdmin)
admin.site.register(Week5, WeekAdmin)
admin.site.register(Week6, WeekAdmin)
admin.site.register(Week7, WeekAdmin)
admin.site.register(Week8, WeekAdmin)
admin.site.register(Week9, WeekAdmin)
