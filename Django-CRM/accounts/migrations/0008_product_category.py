# Generated by Django 3.0.4 on 2020-03-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200325_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
