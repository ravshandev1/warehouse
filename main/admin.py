from django.contrib import admin
from .models import Product, ProductMaterial, Warehouse, Material


admin.site.register([Product, ProductMaterial, Warehouse, Material])
