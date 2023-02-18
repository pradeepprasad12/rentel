
from django.urls import path,include
from Bookingproduct import views

urlpatterns = [
    path('', views.book_product,name="book_product"),
]
