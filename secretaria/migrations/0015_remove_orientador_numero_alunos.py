# Generated by Django 2.2.1 on 2019-12-15 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0014_remove_tema_numero_alunos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orientador',
            name='numero_alunos',
        ),
    ]
