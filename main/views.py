from django.shortcuts import render
from product.models import Product

# Create your views here.
def home(request):
    template_name = 'main/home.html'
    products=Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, template_name, context)