# Generated by Django 2.2.1 on 2019-06-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0015_auto_20190622_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
