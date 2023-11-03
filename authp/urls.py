from django.urls import path
from . import views as authp_views
from store import views as store_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/',authp_views.register,name='register'),
    path('accounts/profile/',authp_views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),

    path('', store_views.home, name='home'),
    path('products/', store_views.product_list, name='product-list'),
    path('products/<int:id>/', store_views.product_detail, name='product-detail'),
    path('products/<int:id>/update/', store_views.edit_product, name='product-update'),
    path('products/create/', store_views.create_product, name='product-create'),
    path('products/<int:id>/delete/', store_views.delete_product, name='product-delete'),
    path('orders/', store_views.view_orders, name='order-list'),
    path('orders/<int:id>/', store_views.view_order, name='order-detail'),
    path('orders/create/', store_views.create_order, name='order-create'),
    path('orders/create/<int:id>/', store_views.create_spot_order, name='order-spot-create'),
    path('orders/<int:id>/delete/', store_views.delete_order, name='order-delete'),
    path('payments/create/<int:id>/', store_views.payment, name='payment'),

]