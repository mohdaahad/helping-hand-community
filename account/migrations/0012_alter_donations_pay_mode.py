# Generated by Django 4.1.7 on 2023-05-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_donations_pay_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='pay_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Cheque', 'Cheque'), ('Net Banking', 'Net Banking')], default='UPI', max_length=11),
        ),
    ]
