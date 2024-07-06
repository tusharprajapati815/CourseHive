from django.shortcuts import render, get_object_or_404
from App.models import Course, Review
# Create your views here.

def home(request, category_name=None):
    courses = Course.objects.all()
    reviews = Review.objects.all()
    categories = Course.objects.values_list('name', flat=True).distinct()
    if category_name:
        courses = courses.filter(name=category_name)
    context = {
        "courses": courses,
        'reviews': reviews,
        'categories': categories,
        'selected_category': category_name
    }
    return render(request, 'home.html', context)

def course_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        courses = Course.objects.filter(name__icontains=search_query)
        context = {'courses': courses, 'search_query': search_query}
        return render(request, 'home.html', context)
    # return render(request, 'course_search.html')

