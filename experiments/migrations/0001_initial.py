# Generated by Django 5.2 on 2025-04-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('wavelength', models.FloatField(help_text='Wavelength in nm')),
                ('power', models.FloatField(help_text='Power in mW')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
