# Generated by Django 4.2.8 on 2024-01-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_forwardphysicaltextcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuturesSubTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exch_rate', models.CharField(max_length=250, null=True)),
                ('value', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FuturesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('futures_price', models.CharField(max_length=250, null=True)),
                ('time', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MysteelTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysteel_index', models.CharField(max_length=250, null=True)),
                ('previous_day', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OnshoreValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column1', models.CharField(max_length=250, null=True)),
                ('Rizhao_rmb', models.CharField(max_length=250, null=True)),
                ('usd_equiv1', models.CharField(max_length=250, null=True)),
                ('caofeidien', models.CharField(max_length=250, null=True)),
                ('usd_equiv2', models.CharField(max_length=250, null=True)),
                ('jiangyin', models.CharField(max_length=250, null=True)),
                ('usd_equiv3', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtherProductValuesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_product_values', models.CharField(max_length=250, null=True)),
                ('period_mar', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortSideIron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=250, null=True)),
                ('port', models.CharField(max_length=250, null=True)),
                ('product', models.CharField(max_length=250, null=True)),
                ('t_p', models.CharField(max_length=250, null=True)),
                ('t_p_on_16th', models.CharField(max_length=250, null=True)),
                ('contents', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortSideIronTextCard1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortSideIronTextCard2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PremOrDiscTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prem_disc', models.CharField(max_length=250, null=True)),
                ('product', models.CharField(max_length=250, null=True)),
                ('phys_in_rmb', models.CharField(max_length=250, null=True)),
                ('rz_value', models.CharField(max_length=250, null=True)),
                ('diff1', models.CharField(max_length=250, null=True)),
                ('diff1_usd', models.CharField(max_length=250, null=True)),
                ('cfd_value', models.CharField(max_length=250, null=True)),
                ('diff2', models.CharField(max_length=250, null=True)),
                ('diff2_usd', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryvsSecondaryDifferentialTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_vs_secondary_differential', models.CharField(max_length=250, null=True)),
                ('apr', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyBlendTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_blend', models.CharField(max_length=250, null=True)),
                ('iocj_ssf_vs_pbf', models.CharField(max_length=250, null=True)),
                ('rz', models.CharField(max_length=250, null=True)),
                ('cfd', models.CharField(max_length=250, null=True)),
                ('jyn', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondary_offer', models.CharField(max_length=250, null=True)),
                ('depth_mt', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]