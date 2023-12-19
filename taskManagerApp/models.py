from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    # Automatically generate a slug based on the title before saving the TodoItem.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TodoItem, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
