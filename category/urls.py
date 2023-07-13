from django.urls import path
# from main.views.dashboard_view import Dashboard
from . import views

urlpatterns = [
   
path('cat-list/', views.cat_list, name='cat_list'),
path('cat-add/', views.cat_add, name='cat_add'),
path('cat-edit/<cat_id>/', views.cat_edit, name='cat_edit'),

path('update-category-status/', views.update_cat_status, name='cat_status'),
path('cat-active/<cat_id>/', views.category_active, name='category_active'),
path('cat-inactive/<cat_id>/', views.category_inactive, name='category_inactive'),
path('cat-delete/<cat_id>/', views.cat_delete, name='cat_delete'),

]