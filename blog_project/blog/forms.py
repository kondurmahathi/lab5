from django import forms
from .models import Post
from .models import Post, Comment, Rating

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']