from rest_framework import viewsets
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
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductVariantSerializer,
    VariantNameSerializer,
    VariantValueSerializer,
    VariantSerializer,
    ProductImageSerializer,
    ProductReviewSerializer,
)
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]


class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    # permission_classes = [IsAuthenticated]


class VariantNameViewSet(viewsets.ModelViewSet):
    queryset = VariantName.objects.all()
    serializer_class = VariantNameSerializer
    # permission_classes = [IsAuthenticated]


class VariantValueViewSet(viewsets.ModelViewSet):
    queryset = VariantValue.objects.all()
    serializer_class = VariantValueSerializer
    # permission_classes = [IsAuthenticated]


class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    # permission_classes = [IsAuthenticated]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    # permission_classes = [IsAuthenticated]


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    # permission_classes = [IsAuthenticated]
