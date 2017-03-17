from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


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
        return '%s %s %s' % (self.BBG, self.lastUpdate, self.Close)


@python_2_unicode_compatible  # only if you need to support Python 2
class calendar(models.Model):
    date = models.DateField()
    cdr = models.CharField(max_length=2)

    def __str__(self):
        return '%s %s' % (self.cdr, self.date)


@python_2_unicode_compatible  # only if you need to support Python 2
class batch_run(models.Model):
    BBG = models.CharField(max_length=12)
    CDR = models.CharField(max_length=12)
    web_source = models.CharField(max_length=12, null=True, blank=True)
    IDX = models.CharField(max_length=12)
    isWorking = models.BooleanField()
    mnemo = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.BBG, self.CDR, self.web_source, self.IDX, self.isWorking)










