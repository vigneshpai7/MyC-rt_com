# Generated by Django 3.1.2 on 2021-02-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=50000)),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('adress', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('pincode', models.CharField(max_length=500)),
            ],
        ),
    ]
