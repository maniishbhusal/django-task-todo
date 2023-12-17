from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth import authenticate

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
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        # Check if passwords match
        if password != password2:
            raise forms.ValidationError('Passwords do not match.')

        # Check if password length is at least 5 characters
        if len(password) < 5:
            raise forms.ValidationError(
                'Password must be at least 5 characters long.')

        # Call the clean method of the parent class
        return super(UserRegistrationForm, self).clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if email already exists in the User model
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')

        return email


class UserLoginForm(forms.Form):
    email = forms.EmailField()  # Field for user email
    # Field for user password
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  # Associate the form with the CustomUser model
        # Specify the fields to be included in the form
        fields = ('email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Authenticate the user using the provided email and password
        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError('Invalid email or password.')

        self.cleaned_data['user'] = user

        # Call the clean method of the parent class
        return super(UserLoginForm, self).clean()
