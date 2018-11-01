from django.contrib import admin
from .models import Consultant, Shop, Director
# Register your models here.

admin.site.register(Shop)
admin.site.register(Director)
admin.site.register(Consultant)
