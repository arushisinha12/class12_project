"""
URL configuration for travelplanner project.

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
from registrations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.first),
    path('page2/',views.second, name='page2'),
    path('page3/', views.third, name='page3'),
    path('name-form/', views.my_view, name='name_form'),
    path('travel-planner/', views.travel_planner, name='travel_planner'),
    path('place/<int:place_id>/', views.page4, name='page4'),
    #path('place/<int:place_id>/<str:email_global>/', views.page4, name='page4'),
    path('page5/', views.page5, name='page5'),
    #path('confirm_booking/<str:key>/', views.confirm_booking, name='confirm_booking'),
]
