# Generated by Django 2.2.3 on 2019-07-04 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190703_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('date_joined',)},
        ),
    ]
