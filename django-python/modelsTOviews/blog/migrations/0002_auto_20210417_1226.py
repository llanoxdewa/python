# Generated by Django 3.2 on 2021-04-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='nama@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
