# Generated by Django 4.1.7 on 2023-02-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, default='title', max_length=255, null=True, verbose_name='Note title'),
        ),
    ]