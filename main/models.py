from __future__ import unicode_literals
from django.utils import timezone
# import datetime
from django.db import models
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.





class Article(models.Model):
    header_text = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    pubDate = models.DateTimeField('dataPublished', default=timezone.now)
    photo = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.header_text


class Master(models.Model):
    name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    years_old = models.IntegerField()
    about = models.TextField()
    his_photo = models.FileField(null=True, blank=True)
    experience = models.IntegerField()
    city = models.CharField(max_length=100)
    link_on_works = models.TextField()

    # his_works = models.ForeignKey(MastersWorks, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




class Topic(models.Model):
    topic_header_text = models.CharField(max_length=100)
    topic_count_of_records = models.IntegerField(default=0)
    topic_pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.topic_header_text






class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Product(models.Model):
    name_of_product = models.CharField(max_length=100)
    sale = models.BooleanField()
    price = models.FloatField ()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_in_stock = models.BooleanField()
    photo = models.FileField(null=True, blank=True)
    info=models.TextField()


    def __str__(self):
        return self.name_of_product
# class Cart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#

# class MyUser(AbstractUser):
#     photo=models.FileField(null=True, blank=True)
#     # cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
class Comments(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    comments_text_of_comment= models.TextField()
    comments_pub_date = models.DateTimeField('date published', default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


    def __str__(self):
        return self.topic.topic_header_text

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # validators = r'((\+380)?(\d+){9})|(\d+){9}'
    mobil_number=models.CharField(max_length=10, null=True)
    # mobil_number=models.CharField(validators=r'((\+380)?(\d+){9})|(\d+){9}', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
        # order_date=models.DateTimeField('date ordered', default=timezone.now)
    def __str__(self):
        return 'User: {0}\n Product: {1}'.format(self.user.username, self.product.name_of_product)