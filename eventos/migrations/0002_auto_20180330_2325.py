# Generated by Django 2.0.2 on 2018-03-31 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo')),
                ('autores', models.ManyToManyField(to='eventos.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('eventoPrincipal', models.CharField(max_length=50, verbose_name='eventoPrincial')),
                ('sigla', models.CharField(max_length=50, verbose_name='sigla')),
                ('dataEHoraDeInicio', models.DateTimeField()),
                ('palavraChave', models.CharField(max_length=50, verbose_name='palavraChave')),
                ('logoTipo', models.CharField(max_length=50, verbose_name='logoTipo')),
                ('cidade', models.CharField(max_length=50, verbose_name='cidade')),
                ('uf', models.CharField(max_length=50, verbose_name='uf')),
                ('endereco', models.CharField(max_length=50, verbose_name='endereco')),
                ('cep', models.CharField(max_length=50, verbose_name='cep')),
            ],
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Evento')),
                ('issn', models.CharField(max_length=50, verbose_name='issn')),
            ],
            bases=('eventos.evento',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Pessoa'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.EventoCientifico'),
        ),
    ]