from django.shortcuts import redirect, render
from .models import Product, ProductGallery, Variation
from .forms import ProductForm, VariationForm
from django.contrib import messages


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context={
        'products':products
    }
    return render(request, "product/product_list.html", context)


def product_add(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # staff=staffForm.save(commit=False)
            #     staff.admin=user
            #     staff=staff.save()
            messages.success(request, "product Successfully Added!")

            return redirect('/product/product-list/')
    context={
        'form':form,
    }
    return render(request, "product/product_add.html", context)




def product_edit(request, pro_id):
    data = Product.objects.get(pk=pro_id)
    form = ProductForm(instance=data)
    if request.method == "POST":
        data = Product.objects.get(pk=pro_id)
        form = ProductForm(request.POST,request.FILES, instance= data)
        if form.is_valid():
            form.save()       
        messages.success(request, "Porduct Successfully UPDATED!")
        return redirect('/product/product-list/')
    context={
        'form':form,
        'category':data,
    }
    return render(request, "product/product_edit.html", context)


def update_product_status(request):
  pro_id = request.POST.get('id')
  pro_status = request.POST.get('status')
  pro=Product.objects.get(pk=pro_id)
  pro.is_active=pro_status
  pro.save()
  messages.success(request, "Product Status Updated Successfully.")
  return redirect('/product/product-list/')


def product_delete(request,pro_id):
    pro = Product.objects.get(pk=pro_id)
    if request.method == 'POST':
                 pro.delete()
                 messages.success(request, "Product Deleted Successfully.")
                 return redirect('/product/product-list/')
    return render(request, 'product/product_delete.html')



def product_images(request, pro_id):
    product = Product.objects.get(pk=pro_id)
    images = ProductGallery.objects.filter(product=pro_id)
          
    if request.method == "POST":
        image = request.FILES.get('image',None)
        print('id', pro_id)
        gelary = ProductGallery()
        gelary.image= image
        gelary.product = product
        gelary.save()
        messages.success(request, "Images Successfully Added!")
        return redirect('/product/product-images/'+pro_id)
    context={
       
        'product':product,
        'images':images
    }
    return render(request, "product/product_images.html", context)



def product_variations(request, pro_id):
    product = Product.objects.get(pk=pro_id)
    form = VariationForm(instance=product)
    variations = Variation.objects.filter(product_id=pro_id)

    if request.method == "POST":
        form = VariationForm(request.POST)
        porduct_id = request.POST.get('product_id')
        if form.is_valid():
            # form.save()
            attr=form.save(commit=False)
            attr.product_id=porduct_id
            attr=attr.save()
            messages.success(request, "Variation Successfully Added!")
            return redirect('/product/product-variations/'+pro_id)
    context={
       
        'product':product,
        'form':form, 
        'variations':variations
    }
    return render(request, "product/product_variations.html", context)

def variation_delete(request,varia_id):
    # print('product', pro_id)
    pro = Variation.objects.get(pk=varia_id)
    if request.method == 'POST':
       pro.delete()
       messages.success(request, "variation Deleted Successfully.")
       return redirect('/product/product-list/')
    return render(request, 'product/product_delete.html')


def image_delete(request,img_id):
    # print('product', pro_id)
    pro = ProductGallery.objects.get(pk=img_id)
    if request.method == 'POST':
       pro.delete()
       messages.success(request, "Image Deleted Successfully.")
       return redirect('/product/product-list/')
    return render(request, 'product/product_delete.html')
