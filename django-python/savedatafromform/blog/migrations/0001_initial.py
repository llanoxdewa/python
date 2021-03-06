# Generated by Django 3.2 on 2021-06-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('email', models.EmailField(default='your email', max_length=254)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
