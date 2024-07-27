from django.shortcuts import render, redirect
from .models import Event
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Corrected here
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookingForm()  # This should be here for GET requests

    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def contact(request):
    return render(request, 'contact.html')
