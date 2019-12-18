from django import forms
from Ghosts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['is_boast', 'post_content']
