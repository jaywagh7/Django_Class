from django.db import models

# Employee Model
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {'Manager' if self.is_manager else 'Employee'}"

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (${self.price})"

# Order Model
class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=255)
    date_placed = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.order_number} - {'Shipped' if self.is_shipped else 'Pending'}"

# Blog Post Model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_attendees = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} at {self.location}"

# Teacher Model
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    experience = models.PositiveIntegerField(help_text="Enter experience in years")  
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter salary in USD")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"