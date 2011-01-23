from django.contrib.auth.forms import UserCreationForm
from django import forms

class EmailUserCreationForm(UserCreationForm):
    username = forms.EmailField(label="Email", max_length=30,
        help_text = ("Required."),
        error_messages = {'invalid': ("Invalid email or email already registered.")})