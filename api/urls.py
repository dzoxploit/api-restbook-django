from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )
urlpatterns = [
        path('', views.getRoutes),
        path('books/', views.getBooks),
        path('books/create/', views.add_books, name='add-books'),
        path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('books/update/<int:pk>/', views.update_books, name='update-books'),
        path('books/<int:pk>/delete/', views.delete_books, name='delete-books'),
]