# Generated by Django 5.1.1 on 2024-09-30 12:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
