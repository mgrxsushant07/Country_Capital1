from django.shortcuts import render
from django.http import HttpResponse
from .models import Country
# Create your views here.

def home(request):
    all_countries = Country.objects.all()
    countries = []
    for country in all_countries:
        countries.append(country.name)
    return render(request, 'countrycapitalapp/index.html', {
                      'countries': countries
                  })

def detail(request, country):
    choosen_country = Country.objects.get(name=country)
    if choosen_country:
        return render(request, 'countrycapitalapp/detail.html', {
            'country': choosen_country.name,
            'capital': choosen_country.capital,
            'currency': choosen_country.currency,
            'population': choosen_country.population,
            'language': choosen_country.official_language,
        })
    else:
        return HttpResponse('<h2>Country not found</h2>')