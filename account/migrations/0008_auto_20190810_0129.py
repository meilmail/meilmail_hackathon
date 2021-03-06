# Generated by Django 2.2.3 on 2019-08-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190810_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='subscribed',
            field=models.ManyToManyField(blank=True, related_name='_account_subscribed_+', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='subscribe',
            field=models.ManyToManyField(blank=True, related_name='_account_subscribe_+', to='account.Account'),
        ),
    ]
