from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_order = orders.count()
    total_pending = orders.filter(status = 'Pending').count()
    delivered = orders.filter(status = 'Delivered').count()

    context= {'orders': orders, 'customers': customers, 'total_order': total_order,
    'total_pending': total_pending, 'delivered': delivered}

    return render(request, 'accounts/dashboard.html', context)

def product(request): 
    product = Product.objects.all()
    return render(request, 'accounts/product.html', {'product':product})


def customer(request, pk_test): 
    customer = Customer.objects.get(id = pk_test)
    orders = customer.order_set.all()
    total_order = orders.count()

    context={'customer':customer, 'orders': orders, 'total_order':total_order}
    return render(request, 'accounts/customer.html', context)