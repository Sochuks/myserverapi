from django.db import models
# models.py

class Details(models.Model):
    slackUsername = models.CharField(max_length=60)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField()
    def __str__(self):
        return self.slackUsername
