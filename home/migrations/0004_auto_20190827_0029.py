# Generated by Django 2.2 on 2019-08-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190827_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(1, 'True'), (0, 'False')], default=0),
        ),
    ]
