# Generated by Django 2.2.1 on 2019-06-23 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0019_auto_20190623_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]