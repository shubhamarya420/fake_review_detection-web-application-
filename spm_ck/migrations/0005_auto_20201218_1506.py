# Generated by Django 3.1.4 on 2020-12-18 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spm_ck', '0004_auto_20201218_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
