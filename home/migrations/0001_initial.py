# Generated by Django 3.2.8 on 2022-01-24 08:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '1234567890'", regex='^\\d{10}$')])),
                ('desc', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField(help_text='Enter a brief description of the project')),
                ('tech', models.CharField(help_text='Enter comma separated tech stack', max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('img', models.ImageField(upload_to='project/')),
                ('link', models.URLField(blank=True, help_text='Enter the link to the project', null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=90, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name_plural': 'Skills',
                'ordering': ['-rating'],
            },
        ),
    ]
