# Generated by Django 2.2 on 2019-04-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercompany',
            name='city',
            field=models.CharField(default='city', max_length=64),
            preserve_default=False,
        ),
    ]
