# Generated by Django 2.2.1 on 2019-07-01 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0021_curso_duracao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'ordering': ['situacao']},
        ),
        migrations.AddField(
            model_name='tema',
            name='aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Aluno'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='carga_horaria',
            field=models.CharField(default='--', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tema',
            name='numero_alunos',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tema',
            name='situacao',
            field=models.CharField(blank=True, default='Aprovado', max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Proposta_tema',
        ),
    ]