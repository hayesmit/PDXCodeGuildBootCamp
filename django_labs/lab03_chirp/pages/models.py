from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Page(models.Model):
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    date_of_origin = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('pages:home')


# , args=[str(self.id)]s
