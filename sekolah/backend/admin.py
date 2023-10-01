from django.contrib import admin
from backend.models import Sejarah,PrakataKepalaSekolah,VisidanMisi,StrukturOrganisasi, Berita 
# Register your models here.


admin.site.register(Sejarah)
admin.site.register(PrakataKepalaSekolah)
admin.site.register(VisidanMisi)
admin.site.register(StrukturOrganisasi)


#Berita
admin.site.register(Berita)
