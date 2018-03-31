from django.contrib import admin
from .models import PessoaJuridica, PessoaFisica, Autor, EventoCientifico, ArtigoCientifico

# Register your models here.
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Autor)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)
