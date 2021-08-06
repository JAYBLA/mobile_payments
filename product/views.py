from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def product_add(request):
    template_name = 'product/add.html'
    products = Product.objects.all()
    print('products:',products)

    if request.POST:
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user_id=request.user.id
            obj.save()
        return redirect('product:product_add')
    else:                
        form=ProductForm()
        context = {
            'form':form,
            'products':products,
        }
    return render(request, template_name, context)

