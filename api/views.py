from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = [
            {'GET': 'api/books'},
            {'POST': 'api/books/create'},
            {'POST': 'api/users/token'}
        ]
    return Response(routes)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBooks(request):
    books = Book.objects.all()
    serialize = BookSerializer(books, many=True)
    return Response(serialize.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_books(request):
    books = BookSerializer(data=request.data)
 
    # validating for already existing data
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if books.is_valid():
        books.save()
        return Response(books.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)