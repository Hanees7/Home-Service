# Generated by Django 4.0.4 on 2022-05-21 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_project_alter_orders_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='pics')),
                ('first_name', models.CharField(max_length=1111)),
                ('last_name', models.CharField(max_length=1111)),
                ('username', models.CharField(max_length=1111)),
                ('password1', models.CharField(max_length=1111)),
                ('password2', models.CharField(max_length=1111)),
                ('email', models.CharField(max_length=1111)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
