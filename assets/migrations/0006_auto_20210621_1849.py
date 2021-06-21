# Generated by Django 2.1.15 on 2021-06-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='toLocation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='logo',
            name='logo',
            field=models.ImageField(upload_to='static/img/logo'),
        ),
    ]
