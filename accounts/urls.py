from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('verify-email-confirm/<uidb64>/<token>/',
         views.verify_email_confirm, name='verify_email_confirm'),
]
