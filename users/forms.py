from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email','phone', 'country', 'avatar',)