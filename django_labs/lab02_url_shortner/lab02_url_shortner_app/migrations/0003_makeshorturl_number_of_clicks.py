# Generated by Django 2.1.7 on 2019-03-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab02_url_shortner_app', '0002_auto_20190301_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeshorturl',
            name='number_of_clicks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
