# Generated by Django 3.1.4 on 2020-12-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spm_ck', '0005_auto_20201218_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='customer',
        ),
        migrations.AddField(
            model_name='rating',
            name='customer',
            field=models.ManyToManyField(to='spm_ck.Customer'),
        ),
    ]
