# Generated by Django 3.2.4 on 2022-01-07 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=100)),
                ('CartID', models.CharField(blank=True, max_length=20, null=True)),
                ('Platform', models.CharField(blank=True, max_length=20, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Address2', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=20, null=True)),
                ('Zip', models.CharField(blank=True, max_length=20, null=True)),
                ('Phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('LocalSku', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('UPC', models.CharField(blank=True, max_length=100, null=True)),
                ('QualityOnHold', models.IntegerField(default=0)),
                ('ItemName', models.CharField(max_length=300)),
                ('Warehouse', models.CharField(blank=True, max_length=100, null=True)),
                ('Weight', models.FloatField(blank=True, default=0, null=True)),
                ('heigh', models.FloatField(blank=True, default=0, null=True)),
                ('width', models.FloatField(blank=True, default=0, null=True)),
                ('depth', models.FloatField(blank=True, default=0, null=True)),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Avaliable', models.BooleanField(default=True)),
                ('Discontinue', models.BooleanField(default=False)),
                ('UpdateTime', models.DateTimeField(auto_now_add=True)),
                ('UpdateBy', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MerchantSku', models.CharField(blank=True, max_length=100, null=True)),
                ('ManuallyFeedQty', models.IntegerField(default=999999)),
                ('LastFeedTime', models.DateTimeField(auto_now_add=True)),
                ('Remark', models.CharField(blank=True, max_length=100, null=True)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Inventory.customer')),
                ('Inventory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Inventory.inventory')),
            ],
        ),
    ]
