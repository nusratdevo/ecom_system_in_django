
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# User login view
def UserLoginView(request):
    if request.user.is_superuser==1:
           return redirect('admin_dashboard')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid Login Credentials!")
                return redirect('admin_login')
            
        
        
        return render(request, 'auth/login.html')




def LogoutView(request):
    logout(request)
    return redirect('admin_login')

@login_required(login_url = 'admin/login')
def AdminDashboardView(request):
    return render(request, 'auth/dashboard.html')

@login_required(login_url = 'admin/login')
# Create your views here.
def cat_list(request):
    return render(request, "category/catgory_list.html")

@login_required(login_url = 'admin/login')
def cat_add(request):
    return render(request, "category/category_add.html")