from django.urls import path
from . import views
from .views import home, BookList, BookDetail, order_book, SearchResultView, cart, add_to_cart, remove_from_cart,out_of_stock

urlpatterns=[
    path('', home, name='home'),
    path('list/', BookList.as_view(), name='list'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('search/', SearchResultView.as_view(), name='search-results'),
    path('bookdetails/<int:pk>/',BookDetail.as_view(),name='details'),
    path('cart/',cart,name='mycart'),
    path('cat/add/<int:book_id>/',add_to_cart,name='add_to_cart'),
    path('cart/remove/<int:book_id>/',remove_from_cart,name='remove_from_cart'),
    path('order/<int:book_id>/',order_book,name='order'),
    path('out_of_stock/',out_of_stock,name='out_of_stock'),
]