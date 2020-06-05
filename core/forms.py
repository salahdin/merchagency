from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    postText = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))
    postImage = forms.ImageField(required=False,widget=forms.widgets.FileInput(attrs={'placeholder': 'PostImage', 'class': 'form-control'}))

    class Meta:
        model = Post
        exclude = ('postby',)

