from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskManagerApp.urls')),
    path('accounts/', include('accounts.urls')),
]
