"""
Ghost: Boasts, Roasts
    Boolean if boast or roast
    Charfield for content of post
    integer field for up and down votes
    datetime field for submit time
"""
from django.db import models


class Post(models.Model):
    is_boast = models.BooleanField(default=True)
    post_content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)

    def _str_(self):
        return self.content
