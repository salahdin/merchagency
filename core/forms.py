from django import forms
from .models import Post,Service


class PostForm(forms.ModelForm):

    postText = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'm-2 form-control'}))
    postImage = forms.ImageField(required=False,widget=forms.widgets.FileInput(attrs={'placeholder': 'Image', 'class': 'm-2 form-control'}))

    class Meta:
        model = Post
        fields = ('postText', 'postImage')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ('user',)