# Generated by Django 2.0.2 on 2018-03-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataDisplay', '0016_auto_20180328_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='wangyi_news_images',
            name='imgurl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='wangyi_news_images',
            name='note',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]