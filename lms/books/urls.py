from django.urls import path

from .views import home, BookList, BookDetail, order_book

urlpatterns=[
    path('', home, name='home'),
    path('list/', BookList.as_view(), name='list'),
    path('bookdetails/<int:pk>/',BookDetail.as_view(),name='details'),
    path('order/<int:book_id>/',order_book,name='order'),
]