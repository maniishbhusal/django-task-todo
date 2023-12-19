# Import necessary modules and classes
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout, get_user_model
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .models import CustomUser

# Get the User model defined in the project
User = get_user_model()

# View for user registration/signup


def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))  # Redirect authenticated users to index page

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Check if an unverified user with the same email exists
            existing_user_exists = User.objects.filter(
                email=email, email_is_verified=False).exists()

            if existing_user_exists:
                # Send activation email again or display a message
                # You can choose to send the activation email here if needed
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('accounts/acc_active_email.html', {
                    'request': request,
                    'user': existing_user_exists,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(existing_user_exists.pk)),
                    'token': account_activation_token.make_token(existing_user_exists),
                })

                email = EmailMessage(mail_subject, message, to=[email])
                email.content_subtype = "html"  # Main content is now text/html
                try:
                    email.send()
                except Exception as e:
                    # Handle email sending failure
                    messages.error(
                        request, 'Failed to send activation email. Please try again later.')
                    return redirect('signup')

                messages.success(
                    request, 'Activation email sent. Please confirm your email address to complete the registration.')
                return redirect('user_login')

            # If no unverified user with the same email, proceed with creating a new user
            user = CustomUser()
            user.full_name = form.cleaned_data.get('full_name')
            user.email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            if not user.email_is_verified:
                # Send activation email
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('accounts/acc_active_email.html', {
                    'request': request,
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                email = EmailMessage(mail_subject, message, to=[email])
                email.content_subtype = "html"  # Main content is now text/html
                try:
                    email.send()
                except Exception as e:
                    # Handle email sending failure
                    messages.error(
                        request, 'Failed to send activation email. Please try again later.')
                    return redirect('signup')

                messages.success(
                    request, 'Activation email sent. Please confirm your email address to complete the registration.')
                return redirect('user_login')

            # If email is already verified, proceed with the regular flow
            messages.success(request, 'Account created successfully.')
            return redirect('user_login')

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and not user.email_is_verified and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email address has been verified.')
        return redirect(reverse('user_login'))
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect(reverse('signup'))


# View for user login
def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))  # Redirect authenticated users to index page

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # Get the email and password from the form's cleaned data
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Get the user object from the form's cleaned data
            user = form.cleaned_data.get('user')
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('index')

    else:
        # If the request method is not POST, create a new instance of the login form
        form = UserLoginForm()
    # Render the login page with the form
    return render(request, 'accounts/login.html', {'form': form})
