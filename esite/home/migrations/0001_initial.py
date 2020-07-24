# Generated by Django 2.2.9 on 2020-07-09 04:49

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headers', wagtail.core.fields.StreamField([('h_banner', wagtail.core.blocks.StructBlock([('head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The bold header text at the frontpage slider', null=True))], blank=False, icon='title', null=True)), ('h_full', wagtail.core.blocks.StructBlock([('head', wagtail.core.blocks.CharBlock(blank=True, classname='full title', icon='title'))], blank=False, icon='title', null=True)), ('h_code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full', icon='code', null=True))], null=True)),
                ('sections', wagtail.core.fields.StreamField([('s_about', wagtail.core.blocks.StructBlock([('pages', wagtail.core.blocks.StreamBlock([('page', wagtail.core.blocks.StructBlock([('blink', wagtail.core.blocks.CharBlock(blank=True, classname='full')), ('use_image', wagtail.core.blocks.BooleanBlock(default=False, help_text='Use picture instead of blink', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(classname='full', required=False)), ('boxes', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(blank=True, classname='full title', icon='title', null=True)), ('content', wagtail.core.blocks.RichTextBlock(blank=True, classname='full', null=True))], blank=False, null=True))], blank=False, icon='cogs', null=True))], blank=False, null=True))], blank=False, icon='radio-empty', null=True)), ('s_modt', wagtail.core.blocks.StructBlock([('modt', wagtail.core.blocks.CharBlock(classname='full', default="Sky's The Limit", max_length=16))], blank=False, icon='pilcrow', null=True)), ('s_sharingan', wagtail.core.blocks.StructBlock([('show_projects', wagtail.core.blocks.BooleanBlock(default=True, help_text='Whether sh1, sh2, sh3 will be shown on this block', required=False)), ('sharingan1', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', null=True)), ('sharingan2', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', null=True)), ('sharingan3', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', null=True)), ('show_team', wagtail.core.blocks.BooleanBlock(default=False, help_text='Whether the team will be shown on this block', required=False)), ('nyan_title', wagtail.core.blocks.CharBlock(classname='full', default='The Team', max_length=16)), ('members', wagtail.core.blocks.StreamBlock([('member', wagtail.core.blocks.StructBlock([('pic', wagtail.images.blocks.ImageChooserBlock(blank=True, classname='full')), ('name', wagtail.core.blocks.CharBlock(blank=True, classname='full', default='', max_length=16)), ('description', wagtail.core.blocks.CharBlock(classname='full', default='', max_length=128))], blank=False, icon='user', null=True))], blank=False))], blank=False, icon='view', null=True)), ('s_community', wagtail.core.blocks.StructBlock([('admins', wagtail.core.blocks.StreamBlock([('admin', wagtail.core.blocks.StructBlock([('show_admins', wagtail.core.blocks.BooleanBlock(default=True, help_text='Whether the admins will be shown on this block', required=False)), ('title', wagtail.core.blocks.CharBlock(classname='full', default='Admins', max_length=16)), ('mrows', wagtail.core.blocks.StreamBlock([('mrow', wagtail.core.blocks.StructBlock([('members', wagtail.core.blocks.StreamBlock([('member', wagtail.core.blocks.StructBlock([('pic', wagtail.images.blocks.ImageChooserBlock(blank=True, classname='full')), ('name', wagtail.core.blocks.CharBlock(blank=True, classname='full', default='', max_length=16)), ('description', wagtail.core.blocks.CharBlock(classname='full', default='', max_length=128))], blank=False, icon='user', null=True))], required=False))], blank=False, icon='group', null=True))], required=False))], blank=False, icon='group', null=True))])), ('mods', wagtail.core.blocks.StreamBlock([('mod', wagtail.core.blocks.StructBlock([('show_mods', wagtail.core.blocks.BooleanBlock(default=True, help_text='Whether the mods will be shown on this block', required=False)), ('title', wagtail.core.blocks.CharBlock(classname='full', default='Mods', max_length=16)), ('mrows', wagtail.core.blocks.StreamBlock([('mrow', wagtail.core.blocks.StructBlock([('members', wagtail.core.blocks.StreamBlock([('member', wagtail.core.blocks.StructBlock([('pic', wagtail.images.blocks.ImageChooserBlock(blank=True, classname='full')), ('name', wagtail.core.blocks.CharBlock(blank=True, classname='full', default='', max_length=16))], blank=False, icon='user', null=True))], required=False))], blank=False, icon='group', null=True))], required=False))], blank=False, icon='group', null=True))]))], blank=False, icon='group', null=True)), ('s_spaceship', wagtail.core.blocks.StructBlock([], blank=False, icon='pick', null=True)), ('s_gallery', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(blank=True, classname='full')), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(blank=True, classname='full'))]))], blank=False, icon='grip', null=True)), ('s_code', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full'))], blank=False, icon='code', null=True))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomeButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_title', models.CharField(max_length=255, null=True)),
                ('button_embed', models.CharField(blank=True, max_length=255, null=True)),
                ('button_link', models.URLField(blank=True, null=True)),
                ('button_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
        ),
    ]
