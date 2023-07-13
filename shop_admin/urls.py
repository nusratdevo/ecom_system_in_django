from django.urls import path
# from main.views.dashboard_view import Dashboard
from shop_admin.views.auth_view import UserLoginView, LogoutView, AdminDashboardView, cat_list, cat_add

urlpatterns = [
    path('login/', UserLoginView, name='admin_login'),
    path('logout/', LogoutView, name='admin_logout'),
    path('dashboard/', AdminDashboardView, name='admin_dashboard'),
   


]