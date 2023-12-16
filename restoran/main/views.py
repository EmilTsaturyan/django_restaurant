from django.shortcuts import render, redirect
from .models import Contact, Booking, Index, Service, Menu, Team, Testimonial, About

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        count = request.POST.get('count')
        special = request.POST.get('special')
        Booking.objects.create(name=name, email=email, date=date, count=count, special=special)
        return redirect('index')
    index = Index.objects.all().first()
    about = About.objects.all().first()
    menu_list = Menu.objects.all()
    services = Service.objects.all()
    chefs = Team.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'main/index.html', context={
        'index': index,
        'about': about,
        'menu_list': menu_list,
        'services': services,
        'chefs': chefs,
        'testimonials': testimonials
    })

def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        count = request.POST.get('count')
        special = request.POST.get('special')
        Booking.objects.create(name=name, email=email, date=date, count=count, special=special)
        return redirect('index')
    return render(request, 'main/booking.html', context={
        
    })

def about(request):
    about = About.objects.all().first()
    chefs = Team.objects.all()
    return render(request, 'main/about.html', context={
        'about': about,
        'chefs': chefs
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('index')
    return render(request, 'main/contact.html', context={
        
    })

def menu(request):
    menu_list = Menu.objects.all()
    return render(request, 'main/menu.html', context={
        'menu_list': menu_list
    })

def service(request):
    services = Service.objects.all()
    return render(request, 'main/service.html', context={
        'services': services
    })

def team(request):
    chefs = Team.objects.all()
    return render(request, 'main/team.html', context={
        'chefs': chefs
    })

def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'main/testimonial.html', context={
        'testimonials': testimonials
    })