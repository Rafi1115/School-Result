# Generated by Django 3.1.1 on 2020-09-25 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='student',
        ),
    ]
