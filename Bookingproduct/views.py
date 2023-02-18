# from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request,'index.html')

from django.shortcuts import render, redirect
from .models import Product, Booking
from .forms import BookingForm

def book_product(request):
    try:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_product')
        else:
            form = BookingForm()
        products = Product.objects.all()
        bookings = Booking.objects.all()
        context = {
            'form': form,
            'products': products,
            'bookings': bookings,
        }
        return render(request, 'book_product.html', context)
    except Exception as e:
        return render(request, 'book_product.html',{'message':e,'class':'danger'})

