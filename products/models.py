from django.db import models
import os
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
def upload_Prodcut_image(instance, filename):
    ext = filename.split(".")[-1]
    new_filename = f"{str(instance)}_{uuid.uuid4().hex}.{ext}"
    return os.path.join("products", new_filename)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey("products.Category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    variant = models.ForeignKey("products.Variant", on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("product", "variant")
        verbose_name_plural = "product variants"
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return str(self.product) + " " + str(self.variant)


class VariantName(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name


class VariantValue(models.Model):
    value = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name


class Variant(models.Model):
    name = models.ForeignKey("products.VariantName", on_delete=models.CASCADE)
    value = models.ForeignKey("products.VariantValue", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("name", "value")
        verbose_name_plural = "variants"
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return str(self.name) + " " + str(self.value)


class ProductImage(models.Model):
    product_variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=upload_Prodcut_image)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "product images"
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return str(self.product_variant) + " " + self.image.url


class ProductReview(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "product reviews"
        ordering = ["-updated_at", "-created_at"]
        unique_together = ("product", "user")

    def __str__(self):
        return str(self.product) + " Review" + " by " + str(self.user)
