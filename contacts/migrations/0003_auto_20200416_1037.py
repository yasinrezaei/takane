# Generated by Django 3.0.3 on 2020-04-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200416_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
