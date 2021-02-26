
# Generated by Django 3.1.7 on 2021-02-26 10:29


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=1000)),
                ('asset_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mer_name', models.CharField(max_length=100)),
                ('mer_address', models.CharField(max_length=300)),
                ('mer_contactno', models.CharField(max_length=13)),
                ('mer_email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_qty', models.IntegerField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asset.asset')),
            ],
        ),
        migrations.CreateModel(
            name='AssetManagementOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetmgmtout_qty', models.IntegerField()),
                ('assetmgmtout_particulars', models.CharField(max_length=1000)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asset.asset')),
            ],
        ),
        migrations.CreateModel(
            name='AssetManagementIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetmgmtin_date', models.DateField()),
                ('assetmgmtin_billno', models.CharField(max_length=20)),
                ('assetmgmtin_billamount', models.IntegerField()),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asset.merchant')),
            ],
        ),
        migrations.CreateModel(
            name='AssetManagementDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetdet_qty', models.IntegerField()),
                ('assetdet_unitrate', models.IntegerField()),
                ('assetmanagementin', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asset.assetmanagementin')),
            ],
        ),
    ]
