# Generated by Django 2.0.2 on 2018-03-30 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('curriculo', models.CharField(max_length=50, verbose_name='curriculo')),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cpf', models.CharField(max_length=50, verbose_name='cpf')),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cnpj', models.CharField(max_length=50, verbose_name='cnpj')),
                ('razaoSocial', models.CharField(max_length=50, verbose_name='razaoSocial')),
            ],
            bases=('eventos.pessoa',),
        ),
    ]