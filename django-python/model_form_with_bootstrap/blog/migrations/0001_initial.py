# Generated by Django 3.2 on 2021-06-29 10:08

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
                ('nama_lengkap', models.CharField(max_length=20)),
                ('umur', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'laki-laki'), ('female', 'perempuan')], default='perempuan', max_length=20)),
            ],
        ),
    ]
