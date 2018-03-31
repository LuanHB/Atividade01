from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=50)
    email = models.CharField('email', max_length=50)

    def __str__(self):
        return '{}, {}'.format(self.nome, self.email)


class PessoaJuridica(Pessoa):
    cnpj = models.CharField('cnpj', max_length=(50))
    razaoSocial = models.CharField('razaoSocial', max_length=(50))

    def __str__(self):
        return '{}, {}'.format(self.nome, self.cnpj)


class PessoaFisica(Pessoa):
    cpf = models.CharField('cpf', max_length=(50))

    def __str__(self):
        return '{}, {}'.format(self.nome, self.cpf)


class Autor(Pessoa):
    curriculo = models.CharField('curriculo', max_length=(50))

    def __str__(self):
        return '{}, {}'.format(self.nome, self.curriculo)


class Evento(models.Model):
    nome = models.CharField('nome', max_length=(50))
    eventoPrincipal = models.CharField('eventoPrincial', max_length=(50))
    sigla = models.CharField('sigla', max_length=(50))
    dataEHoraDeInicio = models.DateTimeField(blank=False, null=False)
    palavraChave = models.CharField('palavraChave', max_length=(50))
    logoTipo = models.CharField('logoTipo', max_length=(50))
    realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cidade = models.CharField('cidade', max_length=(50))
    uf = models.CharField('uf', max_length=(50))
    endereco = models.CharField('endereco', max_length=(50))
    cep = models.CharField('cep', max_length=(50))

    def __str__(self):
        return '{} - {}'.format(self.nome, self.dataEHoraDeInicio)


class EventoCientifico(Evento):
    issn = models.CharField('issn', max_length=(50))

    def __str__(self):
        return '{}, {}'.format(self.nome, self.issn)


class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=(50))
    autores = models.ManyToManyField(Autor)
    evento = models.ForeignKey(EventoCientifico, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo




