# Generated by Django 3.1.7 on 2021-07-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='desc',
            field=models.TextField(max_length=100),
        ),
    ]