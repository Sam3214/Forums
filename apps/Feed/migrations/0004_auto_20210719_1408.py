# Generated by Django 3.1.7 on 2021-07-19 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Feed', '0003_auto_20210719_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL),
        ),
    ]
