from django.db import models

# Create your models here.
import uuid


class User(models.Model):
    name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=30, unique='True')
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=100, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


class SessionToken(models.Model):
    user = models.ForeignKey(User)
    session_token = models.CharField(max_length=255)
    last_request_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()


class Cart(models.Model):
    user = models.ForeignKey(User)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)

class CartPrdoduct(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    catalogue_id = models.CharField(max_length=50, null=True)


