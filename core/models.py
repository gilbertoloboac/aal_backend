from django.db import models

class Hero (models.Model):
    titulo_hero = models.CharField(max_length=100)
    descricao = models.TextField(max_length=350)
    link = models.URLField(max_length=200)
    imagem = models.ImageField(upload_to='hero')


    def __str__(self):
        return self.titulo_hero

class Noticia (models.Model):
    titulo_noticia = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    foto_noticia = models.ImageField(upload_to='noticia')
    legenda_foto = models.CharField(max_length=200)
    credito_foto = models.CharField(max_length=100)
    olho = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo_noticia
    
class Diretoria (models.Model):
    nome_diretoria = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto_diretoria = models.ImageField(upload_to='diretoria')

    def __str__(self):
        return self.nome_diretoria


class Artigo (models.Model):
    titulo_artigo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    foto_artigo = models.ImageField(upload_to='artigo')
    credito_foto_artigo = models.CharField(max_length=100)
    autor_artigo = models.CharField(max_length=100)
    data_publicacao_artigo = models.DateField(auto_now_add=True)
    texto_artigo = models.TextField()

    def __str__(self):
        return self.titulo_artigo
    
class Agenda (models.Model):
    titulo = models.CharField(max_length=200)
    dia = models.CharField(max_length=2)
    mes = models.CharField(max_length=20)
    horario = models.TimeField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} - {self.horario.strftime('%Hh%M')} - {self.local}"

class GaleriaPresidentes (models.Model):
    foto_presidente = models.ImageField(upload_to='galeria_presidentes')
    nome_presidente = models.CharField(max_length=200)
    ordem_presidencia = models.CharField(max_length=100)
    periodo_presidencia = models.CharField(max_length=100)
   
    
    def __str__(self):
        return f"{self.nome_presidente} - {self.periodo_presidencia}"