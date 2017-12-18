# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#1 model for creating info about user
class personalInfo(models.Model):
    Nickname = models.CharField(max_length = 140)
    BTC = models.FloatField()
    ETH = models.FloatField()
    NEM = models.FloatField()
    XZC = models.FloatField()


