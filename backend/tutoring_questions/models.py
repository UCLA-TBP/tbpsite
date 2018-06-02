from django.db import models
from tutoring.models import Class
from main.models import Profile

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    poster = models.ForeignKey(Profile, blank=True, null=True)
    related_class = models.ForeignKey(Class)
    related_professor = models.CharField(max_length = 30, blank=True, verbose_name="Class Professor")
    image = models.ImageField(upload_to='tutoring_questions_images', null=True, blank=True)

    def __unicode__(self):
        return "(%s) (%s): %s" % (self.related_class, self.poster, self.question_text)

class Comment(models.Model):
    related_question = models.ForeignKey(Question)
    poster = models.ForeignKey(Profile, blank=True, null=True)
    comment_text = models.CharField(max_length=400)
    image = models.ImageField(upload_to='tutoring_questions_images', null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):
        return "(%s) (%s): %s" % (self.related_question.question_text, self.poster, self.comment_text)
