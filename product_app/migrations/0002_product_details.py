# Generated by Django 4.0.4 on 2022-06-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_rate', models.IntegerField()),
                ('product_description', models.CharField(max_length=100)),
                ('product_status', models.CharField(choices=[('none', 'select Status'), ('Male', 'Stock Full'), ('FeMale', 'Out of Stock')], default='Select Status', max_length=30)),
            ],
        ),
    ]
