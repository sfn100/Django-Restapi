# Generated by Django 3.2.4 on 2021-06-29 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0004_auto_20210628_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='userid',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='fullname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='message',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(max_length=11),
        ),
    ]