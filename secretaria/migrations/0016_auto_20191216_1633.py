# Generated by Django 2.2.1 on 2019-12-16 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0015_remove_orientador_numero_alunos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='descricao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Descricao_Nota'),
        ),
    ]
