from django import forms
# import model post
from .models import PostModel, CommentModel

class PostForm(forms.ModelForm):
    class Meta:
        model       = PostModel
        fields      = [
            'title','category','desc','image'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model       = CommentModel
        fields      = [
            'desc'
        ]

