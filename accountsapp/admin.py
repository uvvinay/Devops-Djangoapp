from django.contrib import admin
from .models import Customer,Products,Orders

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','location']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description']
    list_editable = ['price',]
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','product','status',]

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(Orders,OrderAdmin)
