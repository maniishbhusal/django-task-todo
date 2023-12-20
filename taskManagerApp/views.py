from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout


def index(request: HttpRequest) -> render:
    if not request.user.is_authenticated:
        return redirect(reverse('user_login'))

    if request.method == 'POST':
        title = request.POST.get('title')
        try:
            TodoItem.objects.create(title=title, user=request.user)
            messages.success(request, 'Task added successfully!')
        except IntegrityError as e:
            messages.error(request, 'Task already exists!')

    context = {'items': TodoItem.objects.filter(
        user=request.user).order_by('-updated_at')}
    return render(request, 'taskManagerApp/index.html', context=context)


@login_required
def update_item(request, id, slug):
    item = get_object_or_404(TodoItem, pk=id, user=request.user)
    if request.method == 'POST':
        item.title = request.POST.get('title')
        item.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('index')
    context = {'item': item}
    return render(request, 'taskManagerApp/update_item.html', context=context)


@login_required
def delete_item(request, id, slug):
    # Retrieve the TodoItem object with the given slug or raise a 404 error.
    item = get_object_or_404(TodoItem, pk=id, user=request.user)
    item.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('index')


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect(reverse('user_login'))


@csrf_protect
def update_completed(request, item_id, status):
    todo_item = get_object_or_404(TodoItem, id=item_id, user=request.user)
    todo_item.completed = bool(status)
    todo_item.save()

    return JsonResponse({'success': True})
