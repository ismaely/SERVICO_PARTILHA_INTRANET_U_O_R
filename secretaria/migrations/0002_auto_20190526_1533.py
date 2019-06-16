# Generated by Django 2.2.1 on 2019-05-26 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Pessoa')),
                ('numero_estudante', models.CharField(max_length=10)),
                ('faculdade', models.CharField(max_length=14)),
                ('curso', models.CharField(max_length=20)),
                ('ninel_academico', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Pessoa')),
                ('numero_docente', models.CharField(max_length=10)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='secretaria.Pessoa')),
                ('cargo', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='foto',
            field=models.FileField(blank=True, default='user.jpg', null=True, upload_to='foto/'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(default='--', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='municipio',
            field=models.CharField(default='--', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='residencia',
            field=models.CharField(default='--', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(default='--', max_length=20, null=True),
        ),
    ]
