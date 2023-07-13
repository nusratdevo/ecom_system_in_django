from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Category
from .forms import CategoryForm



def cat_list(request):
    category = Category.objects.all()
    context={
        'category':category
    }

    return render(request, "category/cat_list.html", context)


def cat_add(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Successfully Added!")

            return redirect('/category/cat-list/')
    context={
        'form':form,
    }
    return render(request, "category/cat_add.html", context)

def cat_edit(request, cat_id):
    data = Category.objects.get(pk=cat_id)
    form = CategoryForm(instance=data)
    if request.method == "POST":
        data = Category.objects.get(pk=cat_id)
        form = CategoryForm(request.POST,request.FILES, instance= data)
        if form.is_valid():
            form.save()       
        messages.success(request, "Category Successfully UPDATED!")
        return redirect('/category/cat-list/')
    context={
        'form':form,
        'category':data,
    }
    return render(request, "category/cat_edit.html", context)


def update_cat_status(request):
  cat_id = request.POST.get('id')
  cat_status = request.POST.get('status')
  cat=Category.objects.get(pk=cat_id)
  cat.is_active=cat_status
  cat.save()
  messages.success(request, "Category Status Updated Successfully.")
  return redirect('/category/cat-list/')

def category_inactive(request, cat_id):
  cat=Category.objects.get(pk=cat_id)
  cat.is_active='0'
  cat.save()

  messages.error(request, "Category Status inactivate Successfully.")
  return redirect('/category/cat-list/')


def category_active(request, cat_id):
  cat=Category.objects.get(pk=cat_id)
  cat.is_active='1'
  cat.save()
  messages.success(request, "Category Status Updated Successfully.")
  return redirect('/category/cat-list/')


def cat_delete(request,cat_id):
    cat = Category.objects.get(pk=cat_id)
    if request.method == 'POST':
                 cat.delete()
                 messages.success(request, "CAtegory Deleted Successfully.")
                 return redirect('/category/cat-list/')
    return render(request, 'category/cat_delete.html')