from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm

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

def createOrder(request, pk):
    OrderCreateSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=-1)
    
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial = {'customer':customer})
    formSet = OrderCreateSet(instance = customer)
    context = {'form': formSet}

    if request.method == "POST":
        # form = OrderForm(request.POST)
        formSet = OrderCreateSet(request.POST, instance = customer)
        if formSet.is_valid():
            formSet.save()
            return redirect('home')
    return render(request, 'accounts/createupdate.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)
    context = {'form': form}

    if request.method=="POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'accounts/createupdate.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)
    context = {"item":order}
    if request.method=="POST":
        order.delete()
        return redirect('home')
    return render(request, 'accounts/delete.html', context)
