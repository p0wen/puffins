# Generated by Django 3.1.2 on 2020-11-03 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('0', 'Order Received'), ('1', 'Order Accepted'), ('2', 'Preparing for delivery'), ('3', 'Dispatched'), ('4', 'Order Received'), ('C', 'Order Canceld')], default='0', max_length=1),
        ),
    ]
