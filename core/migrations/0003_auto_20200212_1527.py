# Generated by Django 3.0.2 on 2020-02-12 15:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_websitesetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesetting',
            name='contact_us',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='websitesetting',
            name='fees_and_taxes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='websitesetting',
            name='fines',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='websitesetting',
            name='glass_tinting',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='websitesetting',
            name='site_purpose',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='websitesetting',
            name='technical_glance',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
