# Generated by Django 2.2.6 on 2019-10-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accionista', '0002_auto_20190930_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accionista',
            name='fax',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
