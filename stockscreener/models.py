from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


#@python_2_unicode_compatible  # only if you need to support Python 2
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('Date')
#
#    def __str__(self):
#        return self.question_text
#
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
#@python_2_unicode_compatible  # only if you need to support Python 2
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#
#    def __str__(self):
#        return self.choice_text


@python_2_unicode_compatible  # only if you need to support Python 2
class signals(models.Model):
    Date = models.DateField()
    Close = models.FloatField()
    ewma_10 = models.FloatField()
    ewma_20 = models.FloatField()
    ewma_50 = models.FloatField()
    ewma_100 = models.FloatField()
    var = models.FloatField()
    mean = models.FloatField()
    cv = models.FloatField()
    BBG = models.CharField(max_length=12)
    lastUpdate = models.DateTimeField()

    def __str__(self):
        return self.BBG
