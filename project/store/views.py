from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def form(request):
    context = {}
    return render(request, 'store/form.html', context)


def user_designs(request):
    context = {}
    return render(request, 'store/user_designs.html', context)


def about(request):
    context = {}
    return render(request, 'store/about.html', context)


def portfolio(request):
    context = {}
    return render(request, 'store/portfolio.html', context)


def service(request):
    context = {}
    return render(request, 'store/service.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)
