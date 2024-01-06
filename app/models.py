from django.db import models

# Create your models here.


class ForwardPhysicalValues(models.Model):
    prod = models.CharField(max_length=250, null=True)
    mar = models.CharField(max_length=250, null=True)
    apr = models.CharField(max_length=250, null=True)
    may = models.CharField(max_length=250, null=True)
    q3 = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.prod}"


class SeaborneLastTradedLevels(models.Model):
    product = models.CharField(max_length=250, null=True)
    primary = models.CharField(max_length=250, null=True)
    secondary = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.product}"


class ForwardPhysicalTextCard(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.text}"


class PremOrDiscTable(models.Model):
    prem_disc = models.CharField(max_length=250, null=True)
    product = models.CharField(max_length=250, null=True)
    phys_in_rmb = models.CharField(max_length=250, null=True)
    rz_value = models.CharField(max_length=250, null=True)
    diff1 = models.CharField(max_length=250, null=True)
    diff1_usd = models.CharField(max_length=250, null=True)
    cfd_value = models.CharField(max_length=250, null=True)
    diff2 = models.CharField(max_length=250, null=True)
    diff2_usd = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.prem_disc}"


class ProxyBlendTable(models.Model):
    proxy_blend = models.CharField(max_length=250, null=True)
    iocj_ssf_vs_pbf = models.CharField(max_length=250, null=True)
    rz = models.CharField(max_length=250, null=True)
    cfd = models.CharField(max_length=250, null=True)
    jyn = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.proxy_blend}"


class OtherProductValuesTable(models.Model):
    other_product_values = models.CharField(max_length=250, null=True)
    period_mar = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.other_product_values}"


class PrimaryvsSecondaryDifferentialTable(models.Model):
    primary_vs_secondary_differential = models.CharField(max_length=250, null=True)
    apr = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.primary_vs_secondary_differential}"


# class OnshoreValues(models.Model):
#     column1 = models.CharField(max_length=250, null=True)
#     usd_equiv1 = models.CharField(max_length=250, null=True)
#     caofeidien = models.CharField(max_length=250, null=True)
#     usd_equiv2 = models.CharField(max_length=250, null=True)
#     jiangyin = models.CharField(max_length=250, null=True)
#     usd_equiv3 = models.CharField(max_length=250, null=True)

#     def __str__(self) -> str:
#         return f"{self.usd_equiv1}"


class OnshoreValues(models.Model):
    column1 = models.CharField(max_length=250, null=True)
    Rizhao_rmb = models.CharField(max_length=250, null=True)
    usd_equiv1 = models.CharField(max_length=250, null=True)
    caofeidien = models.CharField(max_length=250, null=True)
    usd_equiv2 = models.CharField(max_length=250, null=True)
    jiangyin = models.CharField(max_length=250, null=True)
    usd_equiv3 = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.usd_equiv1}"


class MysteelTable(models.Model):
    mysteel_index = models.CharField(max_length=250, null=True)
    previous_day = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.mysteel_index}"


class FuturesTable(models.Model):
    futures_price = models.CharField(max_length=250, null=True)
    time = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.futures_price}"


class FuturesSubTable(models.Model):
    exch_rate = models.CharField(max_length=250, null=True)
    value = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.exch_rate}"


class SecondaryOffer(models.Model):
    secondary_offer = models.CharField(max_length=250, null=True)
    depth_mt = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.secondary_offer}"


class PortSideIron(models.Model):
    no = models.CharField(max_length=250, null=True)
    port = models.CharField(max_length=250, null=True)
    product = models.CharField(max_length=250, null=True)
    t_p = models.CharField(max_length=250, null=True)
    t_p_on_16th = models.CharField(max_length=250, null=True)
    contents = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.no}"


class PortSideIronTextCard1(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.text}"


class PortSideIronTextCard2(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.text}"
