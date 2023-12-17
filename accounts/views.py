# Import necessary modules and classes
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout, get_user_model

# Get the User model defined in the project
User = get_user_model()

# View for user registration/signup
def signup(request):
    if request.method == 'POST':
        # Create a form instance and populate it with the data from the request
        form = UserRegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # Create a User instance without saving it to the database
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')

            # Set the password for the user and save it to the database
            user.set_password(password)
            user.save()

            # Display a success message and redirect to the login page
            messages.success(request, 'Account created successfully.')
            return redirect('user_login')
    # If the request is not a POST, create an empty form
    else:
        form = UserRegistrationForm()

    # Render the signup form template with the form
    return render(request, 'accounts/signup.html', {'form': form})


# View for user login
def login_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with the data from the request
        form = UserLoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # Get email and password from the form
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user = authenticate(email=email, password=password)
            if user is not None:
                print(email, password)
                login(request, user)
                messages.success(request, 'You are now logged in.')
                return redirect('index')
    # If the request is not a POST, create an empty form
    else:
        form = UserLoginForm()

    # Render the login form template with the form
    return render(request, 'accounts/login.html', {'form': form})
