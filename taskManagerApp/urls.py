from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/<slug:slug>/', views.delete_item, name='delete_item'),
    path('update/<int:id>/<slug:slug>/', views.update_item, name='update_item'),
]
