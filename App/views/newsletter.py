from django.shortcuts import render
import requests
# Create your views here.

API_KEY = '11e43782fe8044d1bd3eec0ac70a4423'

COUNTRY_CODES = {
    'United Arab Emirates': 'ae',
    'Argentina': 'ar',
    'Austria': 'at',
    'Australia': 'au',
    'Belgium': 'be',
    'Bulgaria': 'bg',
    'Brazil': 'br',
    'Canada': 'ca',
    'Switzerland': 'ch',
    'China': 'cn',
    'Colombia': 'co',
    'Cuba': 'cu',
    'Czech Republic': 'cz',
    'Germany': 'de',
    'Egypt': 'eg',
    'France': 'fr',
    'United Kingdom': 'gb',
    'Greece': 'gr',
    'Hong Kong': 'hk',
    'Hungary': 'hu',
    'Indonesia': 'id',
    'Ireland': 'ie',
    'Israel': 'il',
    'India': 'in',
    'Italy': 'it',
    'Japan': 'jp',
    'South Korea': 'kr',
    'Lithuania': 'lt',
    'Latvia': 'lv',
    'Morocco': 'ma',
    'Mexico': 'mx',
    'Malaysia': 'my',
    'Nigeria': 'ng',
    'Netherlands': 'nl',
    'Norway': 'no',
    'New Zealand': 'nz',
    'Philippines': 'ph',
    'Poland': 'pl',
    'Portugal': 'pt',
    'Romania': 'ro',
    'Serbia': 'rs',
    'Russia': 'ru',
    'Saudi Arabia': 'sa',
    'Sweden': 'se',
    'Singapore': 'sg',
    'Slovakia': 'sk',
    'Thailand': 'th',
    'Turkey': 'tr',
    'Taiwan': 'tw',
    'Ukraine': 'ua',
    'United States': 'us',
    'Venezuela': 've',
    'South Africa': 'za'
}


def news_letter(request):
    country = request.GET.get('country', 'United States')  
    category = request.GET.get('category', 'technology')
    country_code = COUNTRY_CODES.get(country, 'us')  

    url = f'https://newsapi.org/v2/top-headlines?apiKey={API_KEY}'

    if country:
        url += f'&country={country_code}'
    if category:
        url += f'&category={category}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', []) 
        
        filtered_articles = [
            article for article in articles
            if article.get('author') and article.get('publishedAt') and article.get('urlToImage') and article.get('title')
        ]
    else:
        data = {}
        filtered_articles = []

    return render(request, 'newsletter.html', context={
        'data': data,
        'articles': filtered_articles,
    })