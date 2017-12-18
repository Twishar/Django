# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
import site
# Register your models here.
from .models import personalInfo

admin.site.register(personalInfo)