from django import forms
from .models import Post,Service


class PostForm(forms.ModelForm):

    postText = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Post', 'class': 'form-control'}))
    postImage = forms.ImageField(required=False, widget=forms.widgets.FileInput(attrs={'placeholder': 'Image', 'class': 'form-control'}))
    PostImageWebLink = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'input image from the web', 'class': 'form-control'}))
    price = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'price of item', 'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('postText', 'postImage')


class ServiceForm(forms.ModelForm):
    Service_name = forms.CharField(required=True,
                               widget=forms.widgets.TextInput(attrs={'id':'', 'placeholder': 'Service name', 'class': 'form-control mb-4'}))
    description = forms.CharField(required=True,
                               widget=forms.widgets.Textarea(attrs={'id':'', 'placeholder': 'Service name', 'class': 'form-control mb-4'}))
    avi = forms.ImageField(required=False, widget=forms.widgets.FileInput(
        attrs={'placeholder': 'Image', 'class': 'form-control'}))
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ('user','createDate')