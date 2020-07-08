# Generated by Django 2.1.7 on 2019-03-22 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('listing_title', models.CharField(blank=True, help_text='Override the page title used when this page appears in listings', max_length=255)),
                ('listing_summary', models.CharField(blank=True, help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Search description' field above is not defined.", max_length=255)),
                ('hero_title', models.CharField(max_length=80, null=True)),
                ('hero_introduction', models.CharField(max_length=255)),
                ('hero_button_text', models.CharField(blank=True, max_length=55)),
                ('articles_text', models.CharField(blank=True, max_length=150, null=True)),
                ('articles_linktext', models.CharField(blank=True, max_length=80, null=True)),
                ('pages_text', models.CharField(blank=True, max_length=150, null=True)),
                ('pages_linktext', models.CharField(blank=True, max_length=80, null=True)),
                ('news_text', models.CharField(blank=True, max_length=150, null=True)),
                ('news_linktext', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='HomePageFeaturedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]