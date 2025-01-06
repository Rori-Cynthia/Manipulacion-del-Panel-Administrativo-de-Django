from django.contrib.auth import login
from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import UserRegistrationForm, BookForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = "registration.html"
    form_class = UserRegistrationForm
    success_message = "Te has registrado correctamente."

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('home'))


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_message = "Has iniciado sesión correctamente."

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class HomeView(TemplateView):
    template_name = 'home.html'


class BookInputView(FormView):
    template_name = 'inputbook.html'
    form_class = BookForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return render(self.request, 'success.html', {'title': form.cleaned_data['title']})
