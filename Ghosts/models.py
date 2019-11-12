"""
Ghost: Boasts, Roasts
    Boolean if boast or roast
    Charfield for content of post
    integer field for up and down votes
    datetime field for submit time
"""
from django.db import models
from django.utils import timezone


class Boasts_Roasts(models.Model):
    is_boast = models.BooleanField()
    post_content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.content
