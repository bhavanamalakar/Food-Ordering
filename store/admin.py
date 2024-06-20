from django.contrib import admin
from .models.Product import Product
from .models.Category import Category
from .models.Customer import Customer
from .models.orders import order
# Register your models here.

# to show fields actual label in admin site view
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(order)  #(order) class name