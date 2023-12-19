from django.contrib.auth.decorators import permission_required
from typing import Dict
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404


def index(request: HttpRequest) -> render:
    if not request.user.is_authenticated:
        return redirect(reverse('user_login'))

    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title, user=request.user)
        messages.success(request, 'Task added successfully!')

    context = {'items': TodoItem.objects.filter(
        user=request.user).order_by('-id')}
    return render(request, 'taskManagerApp/index.html', context=context)


@permission_required('delete_item')
def delete_item(request, id, slug):
    # Retrieve the TodoItem object with the given slug or raise a 404 error.
    item = get_object_or_404(TodoItem, pk=id)
    item.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('index')
