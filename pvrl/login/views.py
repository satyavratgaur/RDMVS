from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from login.models import UserCredentials
from login.forms import UserAuthentication

#Saving information
"""
# Create a new record using the model's constructor.
record = pvrl_user_login(uname="TheGreatestSatu",psw="Amazing")

# Save the object into the database.
record.save()

#Classify field
# Access model field values using Python attributes.
print(record.id) # should return 1 for the first record. 
print(record.my_field_name) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
record.my_field_name = "New Instance Name"
record.save()
"""

## For handling form requests
def user_login(request):
    if request.method == 'POST':
        try:
            user_creds = get_object_or_404(UserCredentials, uname=request.POST['uname'], psw=request.POST['psw'])
            return HttpResponseRedirect('/pvrl/uploads')
        except:
            return HttpResponseRedirect('/pvrl/f-login')

        # user_creds = get_object_or_404(UserCredentials, uname=request.POST['uname'], psw=request.POST['psw'])
        # print(user_creds)
        # if user_creds:
        #     return HttpResponse('hello world')
        # else:
        #     return HttpResponseRedirect(reverse("Invalid Credentials"))



#For creating template
def index(request):
#    View function for home page of site.

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'login.html')

def myView(request):
    return HttpResponse('hello world')
