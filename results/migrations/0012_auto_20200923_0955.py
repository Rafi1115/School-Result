# Generated by Django 3.1.1 on 2020-09-23 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0011_auto_20200923_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='srenii',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.class_alim'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sreni',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.class_dakhil'),
        ),
    ]
