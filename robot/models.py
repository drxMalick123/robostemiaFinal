# from django.db import models
# from django.utils import timezone
# from orderable.models import Orderable  # 👈 Import Orderable


# class Person(Orderable):  # ✅ Inherit from Orderable
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     about = models.TextField()
#     image_url = models.ImageField(upload_to='people/', blank=True, null=True)

#     def __str__(self):
#         return self.name


# class Services(Orderable):  # ✅ Inherit from Orderable
#     name = models.CharField(max_length=100)
#     description = models.TextField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     about = models.TextField()
#     image_url = models.ImageField(upload_to='services/', blank=True, null=True)
#     date_added = models.DateField(default=timezone.now)
#     features_raw = models.TextField(blank=True, null=True)

#     SHOW_HIDE_CHOICES = [
#         ('show', 'Show'),
#         ('hide', 'Hide'),
#     ]
#     visibility = models.CharField(max_length=10, choices=SHOW_HIDE_CHOICES, default='show')

#     def __str__(self):
#         return self.name


# class Product(models.Model):  # ❌ Not using Orderable (optional)
#     name = models.CharField(max_length=255)
#     category = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     date_added = models.DateField(default=timezone.now)
#     image1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     image4 = models.ImageField(upload_to='product_images/', blank=True, null=True)

#     SHOW_HIDE_CHOICES = [
#         ('show', 'Show'),
#         ('hide', 'Hide'),
#     ]
#     visibility = models.CharField(max_length=10, choices=SHOW_HIDE_CHOICES, default='show')

#     def __str__(self):
#         return self.name


# class HomePageImgSlider(Orderable):  # ✅ Inherit from Orderable
#     name = models.CharField(max_length=100)
#     decription = models.CharField(max_length=100)
#     BtnText = models.CharField(max_length=100, default='')
#     Btnlink = models.CharField(max_length=100)
#     image_url = models.ImageField(upload_to='HomePageImgSlider/', blank=True, null=True)

#     def __str__(self):
#         return self.name


# class AdvisoryCommitteeMember(Orderable):  # ✅ Inherit from Orderable
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='advisory/', blank=True, null=True)

#     def __str__(self):
#         return self.name
    

# class ContactMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     date_submitted = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.name} - {self.subject} - {self.date_submitted}" 


# models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    about = models.TextField()
    image_url = models.ImageField(upload_to='people/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # ✅ Required

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    image_url = models.ImageField(upload_to='services/', blank=True, null=True)
    date_added = models.DateField(default=timezone.now)
    features_raw = models.TextField(blank=True, null=True)
    visibility = models.CharField(
        max_length=10,
        choices=[('show', 'Show'), ('hide', 'Hide')],
        default='show'
    )
    order = models.PositiveIntegerField(default=0)  # ✅ Required

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Product(models.Model):  # Not using sortable
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date_added = models.DateField(default=timezone.now)
    image1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    visibility = models.CharField(
        max_length=10,
        choices=[('show', 'Show'), ('hide', 'Hide')],
        default='show'
    )

    def __str__(self):
        return self.name


class HomePageImgSlider(models.Model):
    name = models.CharField(max_length=100)
    decription = models.CharField(max_length=100)
    BtnText = models.CharField(max_length=100, default='')
    Btnlink = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='HomePageImgSlider/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # ✅ Required

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class AdvisoryCommitteeMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='advisory/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)  # ✅ Required

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ScientificCommitteeMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='advisory/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)  # ✅ Required

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.subject} - {self.date_submitted}"




class Costomer_Oder_list_details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)  # ✅ Required

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class UserCartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # One-to-many with User
    product_id = models.IntegerField(default=0)
    product_count = models.IntegerField( default=0)


    def __str__(self):
        return f"{self.user.username} "
    



class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Customer Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    # Address
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    # Order Details
    payment_method = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    estimated_delivery = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='order_items/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} (x{self.quantity})"
