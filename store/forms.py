from django import forms
from django.contrib.auth.models import User
from .models import Product, OrderItem, Payment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'quantity']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSpotForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']

class OrderPaymentForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['paid']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order_details']

