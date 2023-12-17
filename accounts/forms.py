from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    # Password fields with password input widget
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    # Full name field with optional attribute and placeholder
    full_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email', 'password', 'password2')

    # Custom clean method for additional validations
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # Check if passwords match
        if password != password2:
            raise forms.ValidationError('Passwords do not match.')

        # Check if password length is at least 5 characters
        if len(password) < 5:
            raise forms.ValidationError(
                'Password must be at least 5 characters long.')

        # Check if email already exists in the User model
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            raise forms.ValidationError('Email already exists.')

        # Call the clean method of the parent class
        return super(UserRegistrationForm, self).clean()




class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Check if email exists in the User model
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email does not exist.')

        # Check if password is correct
        user = User.objects.get(email=email)

        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password.')

        # Call the clean method of the parent class
        return super(UserLoginForm, self).clean()