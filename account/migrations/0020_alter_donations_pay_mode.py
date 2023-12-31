# Generated by Django 4.1.7 on 2023-09-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_donations_pay_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='pay_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Cheque', 'Cheque'), ('Net Banking', 'Net Banking'), ('CC', 'Credit Card'), ('DC', 'ATM/Debit Card')], default='UPI', max_length=11),
        ),
    ]
