
from django.contrib import admin
from django.urls import path
import store.views
import django.contrib.auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_add/', store.views.product_add),
    path('customer_add/', store.views.customer_add),
    path('order_form/', store.views.order_add),
    path('payment_form/', store.views.payment),
    path('cart_form/', store.views.cart),
    path('review_form/', store.views.review),
    path('home/', store.views.home_view, name='home'),
    path('register/', store.views.register_view),
    path('login/', django.contrib.auth.views.LoginView.as_view(template_name='Login.html')),

]
