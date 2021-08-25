# Generated by Django 3.2.6 on 2021-08-25 11:04

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('B', 'Bishkek'), ('C', 'Chuy'), ('N', 'Naryn'), ('O', 'Osh'), ('I', 'Issykkul'), ('T', 'Talas'), ('A', 'Batken'), ('D', 'DjalalAbad')], max_length=1)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
