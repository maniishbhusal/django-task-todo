from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("placeholder to later display a list of all blogs")
    # return redirect('user_login')
    return render(request, 'taskManagerApp/index.html')

