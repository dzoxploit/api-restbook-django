from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

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
    if request.query_params:
        books = Book.objects.filter(**request.query_params.dict())
    else:
        books = Book.objects.all()
 
    # if there is something in items else raise error
    if books:
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_books(request, pk):
    book = Book.objects.get(pk=pk)
    data = BookSerializer(instance=book, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_books(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_202_ACCEPTED)