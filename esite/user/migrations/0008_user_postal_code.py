# Generated by Django 2.2.3 on 2019-07-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190709_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
