# Generated by Django 5.0.6 on 2024-05-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pack_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('est_connecte', models.BooleanField(default=False)),
            ],
        ),
    ]