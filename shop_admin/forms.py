
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea, SelectMultiple, CheckboxInput

from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','gender','status','profile_pic']
        widgets = {
            'address': Textarea(attrs={'class': 'form-control','placeholder': 'Enter full address'}),
            'mobile': NumberInput(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'status': CheckboxInput(attrs={'class': 'form-control', 'type': 'checkbox'}),
            'profile_pic': FileInput(attrs={'class': 'form-control'}),

        }


     #tags = models.ManyToManyField(Tag, blank=True, related_name='inventory_tag')
     #'tags': SelectMultiple(attrs={'class': 'form-control select2', 'multiple': 'multiple'}),
    #'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Name'}),
     #Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))