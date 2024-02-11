from django.contrib import admin
from .models import Product, Category, ProductVariant, VariantName, VariantValue, Variant, ProductImage, ProductReview

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "category__name")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("product", "variant", "stock_quantity")
    list_filter = ("product", "variant")
    search_fields = ("product__name", "variant__name")

@admin.register(VariantName)
class VariantNameAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")
    search_fields = ("name", "display_name")

@admin.register(VariantValue)
class VariantValueAdmin(admin.ModelAdmin):
    list_display = ("value", "display_name")
    search_fields = ("value", "display_name")

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("name", "value")
    list_filter = ("name", "value")
    search_fields = ("name__name", "value__value")

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product_variant", "image")
    list_filter = ("product_variant",)
    search_fields = ("product_variant__product__name", "image")


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating")
    list_filter = ("product", "user", "rating")
    search_fields = ("product__name", "user__username", "rating")
