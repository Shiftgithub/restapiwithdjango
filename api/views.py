from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Item
from app.models import Product
from .serializers import ItemSerializer
from .serializers import ProductSerializer


@api_view(['GET'])
def getData(request):
    # person = {'name': 'Mamun Mia Turan', 'age': '21'}
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductData(request):
    # person = {'name': 'Mamun Mia Turan', 'age': '21'}
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addIteam(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
