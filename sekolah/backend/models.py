from django.db import models

# Create your models here.
class Sejarah(models.Model):
    judul      = models.CharField(max_length=255)
    keterangan = models.TextField()
    foto       = models.ImageField(upload_to='foto/')
    def __str__(self):
        return self.judul
        
        
        
class PrakataKepalaSekolah(models.Model):
    judul      = models.CharField(max_length=255)
    keterangan = models.TextField()
    foto       = models.ImageField(upload_to='foto/')
    def __str__(self):
        return self.judul


class VisidanMisi(models.Model):
    judul      = models.CharField(max_length=255)
    keterangan = models.TextField()
    foto       = models.ImageField(upload_to='foto/')
    def __str__(self):
        return self.judul

        
class StrukturOrganisasi(models.Model):
    nama    = models.CharField(max_length=255)
    jabatan = models.TextField()
    foto    = models.ImageField(upload_to='foto/')
    def __str__(self):
        return self.nama



#Berita

class Berita(models.Model):
    judul = models.CharField(max_length=255)
    keterangan = models.TextField()
    isi        = models.TextField()
    foto       = models.ImageField(upload_to='fotoberita/')
    update     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.judul

