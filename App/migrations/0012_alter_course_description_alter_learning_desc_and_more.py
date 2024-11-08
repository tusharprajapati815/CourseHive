# Generated by Django 5.0.6 on 2024-06-16 08:28

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='learning',
            name='desc',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.usercourse'),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='desc',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='desc',
            field=tinymce.models.HTMLField(),
        ),
    ]
