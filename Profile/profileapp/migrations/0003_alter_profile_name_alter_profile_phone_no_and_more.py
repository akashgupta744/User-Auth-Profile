# Generated by Django 5.0.1 on 2024-01-30 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_alter_profile_name_alter_profile_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
