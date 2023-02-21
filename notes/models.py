from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default='title',
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    created = models.DateField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        default=1,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])
