# Generated by Django 2.0.2 on 2018-03-28 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataDisplay', '0009_headline_images_abstracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline_images',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
