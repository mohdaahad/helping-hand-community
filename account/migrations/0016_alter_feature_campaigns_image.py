# Generated by Django 4.1.7 on 2023-05-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_donations_donation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature_campaigns',
            name='image',
            field=models.ImageField(upload_to='hhc/static/account/image/featured/'),
        ),
    ]
