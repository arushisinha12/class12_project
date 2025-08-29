from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse
#from django.core.mail import send_mail
#from django_email_confirmation.models import EmailConfirmation

# Create your views here.
#import mysql.connector as mc


#image
def first(request):
    image_path = 'main/yaatra.jpg'  # Replace with the correct path
    context = {'image_path': image_path}
    return render(request, 'main.html', context)

def second(request):
   data=page2.objects.all()
   return render(request,'page2.html',{'data':data})

def third(request):
   data=page3.objects.all()
   return render(request,'page3.html',{'data':data})


def my_view(request):
    if request.method == 'POST':
        form = MyNameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name'] 

            # Process the submitted data (e.g., save to database)
            return render(request, 'success.html', {'first_name': first_name, 'last_name': last_name})
    else:
        form = NameForm()
    return render(request, 'page2.html', {'form': form})


#calender
def my_form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
    else:
        form = MyModelForm()
    return render(request, 'myapp/my_form.html', {'form': form})

#linking 

def travel_planner(request): 
    global email_global
    if request.method == 'POST':
        date = request.POST.get('date_field')  # Get the user-entered date
        email_global = request.POST.get('email_field')
        month_number = date[5:7] # Extract the month from the date (e.g., 05-2023)
        print("Extracted month number:", month_number)
        print("Extracted Email Global:", email_global)
        
        try:
            month = Month.objects.get(M_NO=month_number)
            places = Places.objects.filter(m_no=month_number)
            month_name = month.MONTHS
            print({'places:',places})
        except Month.DoesNotExist:
            month_name = "Month not found"

        return render(request, 'page3.html', {'month_name': month_name,
                                            'places': places,
                                            'email_global': email_global})
    else:
        return render(request, 'page2.html')

def page4(request, place_id):
    print('page4')
    place = Places.objects.get(p_no=place_id)
    #email_global = request.POST.get('email_global')
    print('page4 email=',email_global)
    #email_global= request.context.get('email_global')
    if place.hotels is None:
        hotels_list = []
    else:
        hotels_list = place.hotels.split(',')
    #send_confirmation_email(email_global)
    # Handle form submission if the request method is POST
    #selected_hotels = request.POST.getlist('hotels')
    return render(request, 'page4.html', {'place': place, 'hotels_list': hotels_list})

def page5(request):
    #email = request.POST.get('email_global')
    return render(request,'page5.html')
