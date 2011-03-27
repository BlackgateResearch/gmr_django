from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from radio.forms import EmailUserCreationForm
from django.contrib.auth.models import User

def index(request):
    '''
    TODO: Replace with generic view?
    '''
    return render_to_response('index.html')


def register(request):
    '''
    Provides the registration functionality to signup users.s
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

    return render_to_response('radio/register.html', {
        'form': form,
    })
