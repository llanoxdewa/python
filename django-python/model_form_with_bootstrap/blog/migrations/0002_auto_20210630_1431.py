# Generated by Django 3.2 on 2021-06-30 07:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='nama_lengkap',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='umur',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.CharField(choices=[('gosip', 'Gosip'), ('berita', 'Berita'), ('Olahraga', 'Olahraga')], default='perempuan', max_length=20),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='judul',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='publish',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]