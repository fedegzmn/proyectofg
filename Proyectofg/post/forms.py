from django.forms import ModelForm

from post.models import Post
from post.models import Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['date_posted']