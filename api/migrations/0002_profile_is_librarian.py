# Generated by Django 3.1 on 2020-10-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_librarian',
            field=models.BooleanField(default=False),
        ),
    ]
