from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
@login_required
def index(request):
    try:
        User = get_user_model()
        user = User.objects.get(pk=request.user.pk)
    except Exception as e:
        # Handle the exception here
        user = None
    if user.is_authenticated:
        return render(request, 'taskManagerApp/index.html')
    return redirect('user_login')
