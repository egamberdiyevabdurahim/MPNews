# Generated by Django 5.1.1 on 2024-09-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_authormodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='views_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]