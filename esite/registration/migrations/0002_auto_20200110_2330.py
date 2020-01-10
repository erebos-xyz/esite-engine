# Generated by Django 2.2.9 on 2020-01-10 22:30

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('home', '0004_auto_20200110_2323'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('registration_head', models.CharField(max_length=255, null=True)),
                ('registration_newsletter_text', models.CharField(max_length=255, null=True)),
                ('registration_privacy_text', wagtail.core.fields.RichTextField(null=True)),
                ('registration_info_text', wagtail.core.fields.RichTextField(null=True)),
                ('registration_step_text', wagtail.core.fields.RichTextField(null=True)),
                ('thank_you_text', wagtail.core.fields.RichTextField(null=True)),
                ('supported_gitlabs', wagtail.core.fields.StreamField([('gitlab_server', wagtail.core.blocks.StructBlock([('organisation', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The owner of gitlab server.', null=True)), ('domain', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The domain of supported gitlab server.', null=True))], blank=False, icon='home', null=True))], null=True)),
                ('registration_button', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.Button')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='registration.FormPage'),
        ),
        migrations.DeleteModel(
            name='RegistrationFormPage',
        ),
    ]
