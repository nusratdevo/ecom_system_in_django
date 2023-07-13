from django import forms
from django.forms import TextInput, Select, FileInput, CheckboxInput,Textarea, NumberInput
from .models import Product, Variation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'product_name': TextInput(attrs={'class': 'form-control',  'placeholder': 'product name','id': 'name'}),
            'slug': TextInput(attrs={'class': 'form-control',  'placeholder': 'product slug','id': 'slug'}),
            'description': Textarea(attrs={'class': 'form-control','placeholder': 'product Description'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'stock': NumberInput(attrs={'class': 'form-control'}),
            'images': FileInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),

            'is_available': CheckboxInput(attrs={'class': 'checkbox', 'id': 'activity'}),
            'bestsellar': CheckboxInput(attrs={'class': 'checkbox', }),
            'toprated': CheckboxInput(attrs={'class': 'checkbox', }),
            'onsale': CheckboxInput(attrs={'class': 'checkbox',})

			#'status': CheckboxInput(attrs={'class': 'form-control', 'type': 'checkbox'}),


        }



class VariationForm(forms.ModelForm):
    class Meta:
        model=Variation
        fields= ['variation_value', 'variation_category', 'is_active']
        widgets = {
            'variation_value': TextInput(attrs={'class': 'form-control','placeholder': 'Enter variation Value'}),
            'variation_category': Select(attrs={'class': 'form-control'}),
            'is_active': CheckboxInput(attrs={'class': 'form-control', 'type': 'checkbox'}),

        }
