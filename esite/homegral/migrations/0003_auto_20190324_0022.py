# Generated by Django 2.1.7 on 2019-03-24 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190322_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='articles_text',
            new_name='articles_title',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='news_text',
            new_name='featured_pages_title',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='pages_text',
            new_name='news_title',
        ),
    ]