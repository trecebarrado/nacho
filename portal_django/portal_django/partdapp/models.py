from django.db import models

class Categoria(models.Model):
    materia = models.CharField(max_length = 150)

class Usuarios(models.Model):
    nombre = models.CharField(max_length = 150)
    clave = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150, unique = True)
    altavalida = models.CharField(max_length = 150, default = 'NO')
    codigo = models.CharField(max_length = 255 , default = '')

class Anuncio(models.Model):
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 2000)
    horario = models.CharField(max_length = 20)
    telefono = models.IntegerField(default = 0)
    email = models.CharField(max_length = 150)
    emailvalido = models.CharField(max_length = 150, default = 'NO')
    precio = models.FloatField(default = 0)
    tfno = models.CharField(max_length = 2)
    mail = models.CharField(max_length = 2)
    foto = models.ImageField(upload_to='images/profile', default = 'images/profile/noperfil.png')
    codigo = models.CharField(max_length = 255)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)

class Chat(models.Model):
    nom = models.CharField(max_length = 150)
    mensaje = models.CharField(max_length = 2000)
