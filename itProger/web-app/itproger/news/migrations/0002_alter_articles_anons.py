# Generated by Django 3.2.10 on 2022-01-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(max_length=250, verbose_name='Anons'),
        ),
    ]
