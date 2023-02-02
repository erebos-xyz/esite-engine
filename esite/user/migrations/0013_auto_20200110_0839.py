# Generated by Django 2.2.9 on 2020-01-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_sources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AddField(
            model_name='user',
            name='customer_id',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]