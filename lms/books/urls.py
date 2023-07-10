from django.urls import path
from . import views
from .views import home, BookList, BookDetail, order_book, SearchResultView, cart, add_to_cart, remove_from_cart, \
    out_of_stock, return_book, order_history, Profile, FinePayment, process_payment

urlpatterns=[
    path('', home, name='home'),
    path('list/', BookList.as_view(), name='list'),
    path('profile/', Profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', SearchResultView.as_view(), name='search-results'),
    path('bookdetails/<int:pk>/', BookDetail.as_view(), name='details'),
    path('cart/', cart, name='mycart'),
    path('cat/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('fine/<int:pk>/', FinePayment.as_view(), name='fine'),
    path('process-payment/<int:order_id>/', process_payment, name='process_payment'),
    path('order/<int:book_id>/', order_book, name='order'),
    path('out_of_stock/', out_of_stock, name='out_of_stock'),
    path('return-book/<int:order_id>/', return_book, name='return_book'),
    path('order-history/', order_history, name='order_history'),

]