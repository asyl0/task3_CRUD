from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'content')
