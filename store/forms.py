from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from store.models import Product
from store.models import Customer
from store.models import Order
from store.models import Payment
from store.models import Cart
from store.models import Reviews


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Pr_ID',
            'Pr_Name',
            'Brand',
            'Price',
            'Category',
            'Image',
            'Description'
        ]


class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'C_ID',
            'Name',
            'Image',
            'Address',
            'Email',
            'Phone',
            'User'
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'O_ID',
            'Cust',
            'Prod',
            'Address',
            'Payment_Status',
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'Payment_ID',
            'Ord',
            'Method',
            'Amount',
        ]


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'Cart_ID',
            'Cust',
            'Prod',
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'Review_ID',
            'Prod',
            'Cust',
            'Rating',
            'Review_Details',
            'Image'
        ]


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ]
