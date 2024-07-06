"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import signupView, loginView
from .import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.home, name='course_list_by_category'),
    path('signup', signupView.as_view(), name = 'signup'),
    path('login', loginView.as_view(), name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('my-courses', views.mycourses, name = 'my-courses'),
    path('course/<str:slug>', views.coursePage, name='coursepage'),
    path('check-out/<str:slug>', views.checkOut, name='checkoutpage'),
    path('verify_payment', views.verifyPayment, name='verify_payment'),
    path('course_search', views.course_search, name='course_search'),
    path('instructor', views.instructor, name='instructor'),
    path('addtocart/<int:cid>', views.addcart, name='addtocart'),
    path('cartlist', views.cart_list, name='cartlist'),
    path('delete/<int:id>',views.Delete_Cartitem, name='delete'),
    path('newsletter', views.news_letter, name='newsletter'),
    path('success', views.success_view, name='success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)