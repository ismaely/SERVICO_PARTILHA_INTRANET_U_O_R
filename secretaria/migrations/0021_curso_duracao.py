# Generated by Django 2.2.1 on 2019-06-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0020_auto_20190623_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='duracao',
            field=models.CharField(default=' ', max_length=2, null=True),
        ),
    ]
