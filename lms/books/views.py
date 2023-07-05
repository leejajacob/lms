from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Book, Order, Cart, CartItems


# Create your views here.
def home(request):
    return render(request, 'index.html')


class BookList(ListView):
    model = Book
    context_object_name = 'book'
    template_name = 'list.html'

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'bookdetails.html'


def PaymentComplete(request, pk):
    product = Book.objects.get(id=pk)
    Order.objects.create(
        product=product
    )
    return JsonResponse('Payment Completed', safe=False)


class SearchResultView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title=query) | Q(author=query)
        )



@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItems.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []

    context = {
        'cart': cart_obj,
        'cart_items': cart_items
    }
    return render(request, 'mycart.html', context)


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj = Cart.objects.create(user=request.user)
    cart_item, created = CartItems.objects.get_or_create(book=book, cart=cart_obj)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('mycart')


@login_required
def remove_from_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_item_qs = CartItems.objects.filter(book=book_id)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
    return redirect('mycart')



def out_of_stock(request):
    return render(request, 'out_of_stock.html')

@login_required
def order_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.quantity > 0:
        user = request.user
        order_date = date.today()
        return_date = order_date + timedelta(days=15)
        fine = 0
        order = Order(user=user, product=book, order_date=order_date, return_date=return_date, fine=fine)
        order.save()
        book.quantity -= 1
        book.save()
        return render(request,'order.html')
    else:
        return redirect('out_of_stock')


@login_required
def return_book(request, order_id):
    order = Order.objects.get(id=order_id)
    today = date.today()
    if today > order.return_date:
        days_late = (today - order.return_date).days
        fine = days_late * 2
        order.fine = fine
        order.save()

    order.delete()
    return render(request, 'order_history.html')

@login_required
def order_history(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'order_history.html', {'orders': orders})