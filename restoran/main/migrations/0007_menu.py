# Generated by Django 5.0 on 2023-12-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_service_icon_class_service_icon_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Food name')),
                ('image', models.ImageField(upload_to='', verbose_name='Food image')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('type', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Launch', 'Launch'), ('Dinner', 'Dinner')], max_length=30, verbose_name='Type')),
            ],
        ),
    ]
