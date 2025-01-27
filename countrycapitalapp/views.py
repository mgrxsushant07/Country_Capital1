from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


data = {
    'india': {
        'capital': 'New Delhi',
        'currency': 'Rupee',
        'population': '1.44B',
        'language': 'Hindi',
    },
    'china': {
        'capital': 'Beijing',
        'currency': 'Yuan',
        'population': '1.42B',
        'language': 'Mandarin',
    },
    'united_states': {
        'capital': 'Washington, D.C.',
        'currency': 'Dollar',
        'population': '343M',
        'language': 'English',
    },
    'indonesia': {
        'capital': 'Jakarta',
        'currency': 'Rupiah',
        'population': '281M',
        'language': 'Indonesian',
    },
    'pakistan': {
        'capital': 'Islamabad',
        'currency': 'Rupee',
        'population': '247M',
        'language': 'Urdu',
    },
    'nigeria': {
        'capital': 'Abuja',
        'currency': 'Naira',
        'population': '227M',
        'language': 'English',
    },
    'brazil': {
        'capital': 'Brasília',
        'currency': 'Real',
        'population': '211M',
        'language': 'Portuguese',
    },
    'bangladesh': {
        'capital': 'Dhaka',
        'currency': 'Taka',
        'population': '171M',
        'language': 'Bengali',
    },
    'russia': {
        'capital': 'Moscow',
        'currency': 'Ruble',
        'population': '145M',
        'language': 'Russian',
    },
    'mexico': {
        'capital': 'Mexico City',
        'currency': 'Peso',
        'population': '129M',
        'language': 'Spanish',
    },
    'ethiopia': {
        'capital': 'Addis Ababa',
        'currency': 'Birr',
        'population': '128M',
        'language': 'Amharic',
    },
    'japan': {
        'capital': 'Tokyo',
        'currency': 'Yen',
        'population': '124M',
        'language': 'Japanese',
    },
    'philippines': {
        'capital': 'Manila',
        'currency': 'Peso',
        'population': '114M',
        'language': 'Filipino',
    },
    'egypt': {
        'capital': 'Cairo',
        'currency': 'Pound',
        'population': '114M',
        'language': 'Arabic',
    },
    'democratic_republic_of_congo': {
        'capital': 'Kinshasa',
        'currency': 'Congolese Franc',
        'population': '106M',
        'language': 'French',
    },
    'vietnam': {
        'capital': 'Hanoi',
        'currency': 'Dong',
        'population': '100M',
        'language': 'Vietnamese',
    },
    'iran': {
        'capital': 'Tehran',
        'currency': 'Rial',
        'population': '90M',
        'language': 'Persian',
    },
    'turkey': {
        'capital': 'Ankara',
        'currency': 'Lira',
        'population': '87M',
        'language': 'Turkish',
    },
    'germany': {
        'capital': 'Berlin',
        'currency': 'Euro',
        'population': '84M',
        'language': 'German',
    },
    'thailand': {
        'capital': 'Bangkok',
        'currency': 'Baht',
        'population': '72M',
        'language': 'Thai',
    },
}

def home(request):
    return render(request, 'countrycapitalapp/index.html', {
                      'countries': list(data.keys())
                  })

def detail(request, country):
    if country in data:
        country_data = data[country]
        return render(request, 'countrycapitalapp/detail.html', {
            'country': country,
            'capital': country_data['capital'],
            'currency': country_data['currency'],
            'population': country_data['population'],
            'language': country_data['language'],
        })
    else:
        return HttpResponse('<h2>Country not found</h2>')