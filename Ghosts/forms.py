from django.db import forms
from GhostPost.models import Post


class PostForm(forms.Form):
    is_Boast = models.BooleanField()
    content = models.CharField()
