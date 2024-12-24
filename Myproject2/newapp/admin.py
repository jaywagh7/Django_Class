from django.contrib import admin
from .models import Employee
from .models import Product
from .models import Order
from .models import BlogPost
from .models import Event
from .models import Teacher
# Register your models here.

from django.contrib import admin
from .models import Employee, Product, Order, BlogPost, Event

# Register the Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'is_manager')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_manager', 'hire_date')

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'date_placed', 'total_amount', 'is_shipped')
    search_fields = ('order_number', 'customer_name')
    list_filter = ('is_shipped', 'date_placed')

# Register the BlogPost model
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published')
    search_fields = ('title', 'author')
    list_filter = ('is_published', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

# Register the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_time', 'end_time', 'max_attendees')
    search_fields = ('title', 'location')
    list_filter = ('start_time', 'end_time')

# Register the Teacher model
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'hire_date', 'phone_number', 'experience', 'salary')
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    list_filter = ('hire_date', 'experience')