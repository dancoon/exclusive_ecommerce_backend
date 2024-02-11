from .models import (
    Product,
    Category,
    ProductVariant,
    VariantName,
    VariantValue,
    Variant,
    ProductImage,
    ProductReview,
)
from rest_framework.serializers import HyperlinkedModelSerializer


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:product-detail"},
        }


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:category-detail"},
        }


class ProductVariantSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:productvariant-detail"},
            "product": {"view_name": "products:product-detail"},
            "variant": {"view_name": "products:variant-detail"},
        }


class VariantNameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VariantName
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:variantname-detail"},
        }


class VariantValueSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = VariantValue
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:variantvalue-detail"},
        }


class VariantSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Variant
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:variant-detail"},
            "name": {"view_name": "products:variantname-detail"},
            "value": {"view_name": "products:variantvalue-detail"},
        }


class ProductImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:productimage-detail"},
            "product_variant": {"view_name": "products:productvariant-detail"},
        }


class ProductReviewSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "products:productreview-detail"},
            "product": {"view_name": "products:product-detail"},
        }
