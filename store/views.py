from django.shortcuts import render, HttpResponse, redirect

from store.forms import ProductAddForm
from store.forms import CustomerAddForm
from store.forms import OrderForm
from store.forms import PaymentForm
from store.forms import CartForm
from store.forms import ReviewForm
from store.forms import RegistrationForm


def product_add(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        form.save()

    form = ProductAddForm()

    context = {
        'product_add_form': form,
    }

    return render(request, 'ProductAdd.html', context)


def customer_add(request):
    if request.method == 'POST':
        form = CustomerAddForm(request.POST)
        form.save()

    form = CustomerAddForm()

    context = {
        'customer_add_form': form,
    }

    return render(request, 'SignUp.html', context)


def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.save()

    form = OrderForm()

    context = {
        'order_add_form': form,
    }

    return render(request, 'Order.html', context)


def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        form.save()

    form = PaymentForm()

    context = {
        'payment_form': form,
    }

    return render(request, 'Payment.html', context)


def cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        form.save()

    form = CartForm()

    context = {
        'cart_form': form,
    }

    return render(request, 'Cart.html', context)


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.save()

    form = ReviewForm()

    context = {
        'review_form': form,
    }

    return render(request, 'Review.html', context)


def home_view(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # if form.is_valid():
        form.save()
        return redirect('home')
    form = RegistrationForm()

    context = {
        'register_form': form,
    }

    return render(request, 'AdminLogin.html', context)
