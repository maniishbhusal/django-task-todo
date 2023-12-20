from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/<slug:slug>/', views.delete_item, name='delete_item'),
    path('update/<int:id>/<slug:slug>/', views.update_item, name='update_item'),
    path('logout/', views.logout_user, name='logout'),
    path('update-completed/<int:item_id>/<int:status>/', views.update_completed, name='update_completed'),
]
