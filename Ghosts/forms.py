from django.db import forms
from GhostPost.models import Boasts_Roasts


class Boasts_Roasts(forms.Form):
    is_boast = forms.BooleanField(required=False)
    post_content = forms.CharField(max_length=280)


class Boasts_Roasts(forms.ModelForm):
    class Meta:
        model = Boasts_Roasts
        fields = ['Boasts', 'content']
