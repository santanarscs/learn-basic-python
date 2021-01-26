from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.api.viewsets import BooksViewSet

route = routers.DefaultRouter()
route.register(r'books', BooksViewSet, basename="Books")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
