from django.db import models
from django.utils import timezone

# Create your models here.

class ArticlesDb(models.Model):
    shortname = models.CharField(max_length=50)
    title = models.CharField(max_length=300)    
    link = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    time_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s"%(self.shortname, self.time_date)