# Generated by Django 2.2.1 on 2019-06-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0018_auto_20190622_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]