from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=30, label='Title')
    description = forms.CharField(
        max_length=250, 
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        label='Description',
        required=False
        )
    # photo = forms.ImageField(upload_to='pictures/%Y_%m/')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select category...'
        )
    is_public = forms.BooleanField(
        label='Publish directly?', 
        required=False, 
        initial=True
        )
    
    class Meta:
        fields = ('title', 'description', 'category', 'is_public')
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

