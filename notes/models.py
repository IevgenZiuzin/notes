from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(
        verbose_name='Note title',
        max_length=255,
        blank=True,
        null=True,
        default='title',
        help_text="Note title"
    )
    text = models.TextField(
        verbose_name='Note content',
        blank=True,
        null=True,
        help_text="Note content"
    )
    created = models.DateField(
        verbose_name='Note created',
        help_text="Note created",
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        default=1,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Author',
        help_text='Author'
    )

    def __str__(self):
        return self.title
