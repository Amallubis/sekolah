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

class PrakataKepalaSekolahsmp(models.Model):
    judul      = models.CharField(max_length=255)
    keterangan = models.TextField()
    fotosmp       = models.ImageField(upload_to='foto/')
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


#kurikulum
class Kurikulum(models.Model):
    pass



#settingan 
#Haeder 
class Header(models.Model):
    judul = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='header/')

    def __str__(self):
        return self.judul
    

    
#footer
class Footer(models.Model):
    judul = models.CharField(max_length=255)
    alamat= models.TextField()
    email = models.EmailField(default='') 
    nohp  = models.CharField(max_length=12)
    fb    = models.CharField(max_length=200)
    ig    = models.CharField(max_length=200)
    tw    = models.CharField(max_length=200)

    def __str__(self):
        return self.judul