from django.db import models
from merchant.models import Merchant
from asset.models import Asset
from assetmanagementin.models import AssetManagementIn

# Create your models here.
class Asset(Models.model):
    # staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    asset_name = models.CharField(max_length=1000)
    asset_description = models.CharField(max_length=1000)

    def __str__(self):
        return "%s %s" % (
        self.asset_name, self.asset_description)


class AssetManagementIn(Models.model):
    merchant = models.ForeignKey(Merchant, on_delete=models.RESTRICT)
    assetmgmtin_date = models.DateField()
    assetmgmtin_billno = models.CharField(max_length=20)
    assetmgmtin_billamount = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s" % (
        self.merchant, self.assetmgmtin_date, self.assetmgmtin_billno, self.assetmgmtin_billamount)


class AssetManagementDetails(Models.model):
    assetmanagementin = models.ForeignKey(AssetManagementIn, on_delete=models.RESTRICT)
    assetdet_qty = models.IntegerField()
    assetdet_unitrate = models.IntegerField()

    def __str__(self):
        return "%s %s %s" % (
        self.assetmanagementin, self.assetdet_qty, self.assetdet_unitrate)


class AssetManagementOut(Models.model):
    asset = models.ForeignKey(Asset, on_delete=models.RESTRICT)
    assetmgmtout_qty = models.IntegerField()
    assetmgmtout_particulars = models.CharField()

    def __str__(self):
        return "%s %s %s" % (
        self.asset, self.assetmgmtout_qty, self.assetmgmtout_particulars)


class Stock(Models.model):
    asset = models.ForeignKey(Asset, on_delete=models.RESTRICT)
    stock_qty = models.IntegerField()

    def __str__(self):
        return "%s %s" % (
        self.asset, self.stock_qty)


class Merchant(Models.model):
    mer_name = models.CharField(max_length=100)
    mer_address = models.CharField(max_length=300)
    mer_contactno = models.CharField(max_length=13)
    mer_email = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s %s" % (
        self.mer_name, self.mer_address, self.mer_contactno, self.mer_email)