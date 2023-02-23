from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default='title',
        help_text='Note title',
        verbose_name='Note title'
    )
    text = models.TextField(
        blank=True,
        null=True,
        help_text='Note text',
        verbose_name='Note text'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text='Note created',
        verbose_name='Note created'
    )
    author = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE,
        help_text='Note author',
        verbose_name='Note author'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])
