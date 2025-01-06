from django.urls import path

from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    HomeView,
    BookInputView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registro/', UserRegistrationView.as_view(), name='registro'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('inputbook/', BookInputView.as_view(), name='inputbook'),
]
