from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()

        send_mail("Регистрация", "Регистрация пройдена, поздравляем!",
                  "noreply@myproject.com", [user.email])

        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserProfileView(UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user