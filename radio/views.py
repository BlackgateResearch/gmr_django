'''
Radio & Site-based views
'''
from django.shortcuts import redirect
from radio.forms import EmailUserCreationForm
from django.contrib.auth.models import User

from annoying.decorators import render_to


@render_to('index.html')
def index(request):
    '''TODO: Replace with generic view?'''
    return {}


@render_to('radio/register.html')
def register(request):
    '''
    Provides the registration functionality to signup users.
    '''
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = User.objects.create_user(email, email, password)
            return redirect('/radio/') # Redirect after POST
        
    else:
        form = EmailUserCreationForm() # An unbound form

    return {'form': form,}
