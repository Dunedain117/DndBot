from django.db import models

class hint(models.Model):
    title = models.CharField(max_length=200)
    time_sent = models.DateTimeField()
    is_sent = models.BooleanField()
    score = models.DurationField()
    def __str__(self):
        return self.title

class team_score(models.Model):
    name = models.CharField(max_length=600)
    score = models.BigIntegerField()
    def __str__(self):
        return self.name
    

# Create your models here.
