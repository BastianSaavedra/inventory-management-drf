from django.db import models

# Create your models here.

"""
models:
    - Customer
    - Supplier
    - Category
    - Product
    - Sale
"""


class Customer(models.Model):
    name = models.CharField(max_lenght=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_numer = models.CharField(max_lenght=10, null=True, blank=True)
    address = models.TextField()

    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_plural_name = "Customers"

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_lenght=100)
    contact_person = models.CharField(max_lenght=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_numer = models.CharField(max_lenght=10, null=True, blank=True)
    address = models.TextField()

    class Meta:
        db_table = "supplier"
        verbose_name = "Supplier"
        verbose_plural_name = "Suppliers"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_lenght=100, unique=True)
    description = models.TextField()

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_plural_name = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_lenght=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_plural_name = "Products"

    def __str__(self):
        return f"{self.name} - {self.category.name} | stock: {self.stock_quantity}"


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "sale"
        verbose_name = "Sale"
        verbose_plural_name = "Sales"

    def __str__(self):
        return f"Sale of {self.product.name} tor {self.customer.name}"
