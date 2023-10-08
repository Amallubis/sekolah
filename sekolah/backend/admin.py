from django.contrib import admin
from backend.models import Sejarah,PrakataKepalaSekolah,PrakataKepalaSekolahsmp,VisidanMisi,StrukturOrganisasi, Berita,Header, Footer,PrestasiSekolah
# Register your models here.


admin.site.register(Sejarah)
admin.site.register(PrakataKepalaSekolah)
admin.site.register(PrakataKepalaSekolahsmp)
admin.site.register(VisidanMisi)
admin.site.register(StrukturOrganisasi)

#prestasi
admin.site.register(PrestasiSekolah)
#Berita
admin.site.register(Berita)

#header
admin.site.register(Header)
admin.site.register(Footer)