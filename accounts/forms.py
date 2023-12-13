from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(), label='电子邮件')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserSettingsForm(UserChangeForm):
    personal_signature = forms.CharField(
        max_length=50, 
        widget=forms.Textarea(attrs={'placeholder': '写一句话作为个性签名吧！'}),
        required=False,
        help_text='最大长度为 50 字',
        label='个性签名',
    )
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'personal_signature']
