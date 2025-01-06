from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import AccountUser, Book


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = AccountUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'valuation']

    def clean_valuation(self):
        valuation = self.cleaned_data.get('valuation')
        if valuation > 10000 or valuation < 0:
            raise forms.ValidationError('La valoración debe estar entre 0 y 10000.')
        return valuation