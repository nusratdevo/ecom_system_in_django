
from django.urls import path

from . import views

urlpatterns = [
   
path('product-list/', views.product_list, name='product_list'),
path('product-add/', views.product_add, name='product_add'),
path('product-edit/<pro_id>/', views.product_edit, name='product_edit'),
path('product-delete/<pro_id>/', views.product_delete, name='product_delete'),

path('product-images/<pro_id>/', views.product_images, name='product_images'),
path('product-variations/<pro_id>/', views.product_variations, name='product_variations'),
path('variation-delete/<varia_id>/', views.variation_delete, name='varia_delete'),
path('image-delete/<img_id>/', views.image_delete, name='image_delete'),



   
]