from .views import UserLoginView, UserRegisterView, UserProfileView
from django.urls import path


app_name = 'users'

urlpatterns = [path('login/', UserLoginView.as_view(), name = 'login'),
               path('register/', UserRegisterView.as_view(), name = 'register'),
               path('profile/', UserProfileView.as_view(), name = 'profile'),]