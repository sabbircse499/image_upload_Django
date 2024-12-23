from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import product
from .serializers import UploadedImageSerializer

@api_view(['GET', 'POST'])
def product_list_create_view(request):
    if request.method == 'GET':
        products = product.objects.all()
        serializer = UploadedImageSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, pk):
    try:
        image = product.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UploadedImageSerializer(image)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UploadedImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        image.delete()
        return Response({"message": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
