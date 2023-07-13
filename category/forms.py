from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput,Textarea
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'category_name': TextInput(attrs={'class': 'form-control',  'placeholder': 'category name','id': 'name'}),
            'slug': TextInput(attrs={'class': 'form-control',  'placeholder': 'category slug','id': 'slug'}),
            'description': Textarea(attrs={'class': 'form-control','placeholder': 'Category Description'}),
            'cat_image': FileInput(attrs={'class': 'form-control'}),
            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'})
			#'status': CheckboxInput(attrs={'class': 'form-control', 'type': 'checkbox'}),


        }
