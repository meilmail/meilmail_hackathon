# Generated by Django 2.2.3 on 2019-08-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190809_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(default='media/default_image.jpg', upload_to=''),
        ),
    ]
