# Generated by Django 4.0 on 2022-01-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', editable=False, upload_to='categories'),
        ),
    ]