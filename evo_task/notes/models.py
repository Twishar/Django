from django.db import models
from django.urls import reverse
# Create your models here.


class Note(models.Model):

    note_title = models.CharField(max_length=250)
    note_body = models.CharField(max_length=1000)
    note_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.note_title + ' - ' + self.note_title

