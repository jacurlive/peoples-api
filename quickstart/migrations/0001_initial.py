# Generated by Django 4.2.7 on 2023-11-24 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('nickname', models.CharField(blank=True, max_length=155, null=True)),
                ('content', models.TextField(blank=True)),
                ('birth_date', models.DateField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.category')),
            ],
        ),
    ]
