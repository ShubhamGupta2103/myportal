# Generated by Django 4.0.6 on 2022-08-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='health_campaign',
            name='pic',
            field=models.FileField(default='', upload_to='appportal/picture'),
        ),
    ]
