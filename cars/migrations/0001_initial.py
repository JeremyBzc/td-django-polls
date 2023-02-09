# Generated by Django 4.1.6 on 2023-02-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('years', models.DateField(verbose_name='Année de construction')),
                ('model', models.CharField(max_length=30)),
                ('version', models.CharField(max_length=50)),
            ],
        ),
    ]