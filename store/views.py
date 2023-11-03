
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Product, OrderItem
from .forms import ProductForm, OrderItemForm, PaymentForm, OrderPaymentForm, OrderSpotForm
import os
def home(request):
    products = Product.objects.all()
    context = {'products':products }
    return render(request, 'home.html', context)

@login_required
def product_detail(request,id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

@login_required
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully')
            return redirect('product-list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'create_product.html', context)

@login_required
def edit_product(request,id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'edit_product.html', context)

@login_required
def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('product-list')

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'Order created successfully')
            return redirect('home')
    else:
        form = OrderItemForm()
    context = {'form': form}
    return render(request, 'create_order.html', context)

@staff_member_required
def payment(request, id):
    order = get_object_or_404(OrderItem, id=id, user=request.user)
    if request.method == 'POST' and request.user.is_staff :
        form = PaymentForm(request.POST)
        form1 = OrderPaymentForm(request.POST, instance=order)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.user = request.user
            staff.save()
            form1.save()
            messages.success(request, 'Payment successful')
            return redirect('home')
    else:
        form = PaymentForm(request.POST)
        form1 = OrderPaymentForm(request.POST, instance=order)
    context = {'form': form, 'form1': form1}
    return render(request, 'edit_order.html', context)

@login_required
def delete_order(request, id):
    order = get_object_or_404(OrderItem, id=id, user=request.user)
    order.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('home')

@login_required
def view_orders(request):
    orders = OrderItem.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'view_orders.html', context)

@login_required
def view_order(request, id):
    order = get_object_or_404(OrderItem, id=id)
    context = {'order': order}
    return render(request, 'view_order.html', context)

@login_required
def create_spot_order(request,id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = OrderSpotForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.save()
            messages.success(request, 'Order created successfully')
            return redirect('home')
    else:
        form = OrderSpotForm()
    context = {'form': form}
    return render(request, 'create_order.html', context)




