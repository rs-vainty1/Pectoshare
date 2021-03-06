# Generated by Django 3.1.8 on 2021-04-23 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('status', models.CharField(blank=True, choices=[('Looking for Work', 'Looking for Work'), ('Employer', 'Employer')], default='Looking for Work', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
