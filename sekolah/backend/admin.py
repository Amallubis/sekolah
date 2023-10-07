from django.contrib import admin
from backend.models import Sejarah,PrakataKepalaSekolah,PrakataKepalaSekolahsmp,VisidanMisi,StrukturOrganisasi, Berita,Header, Footer
# Register your models here.


admin.site.register(Sejarah)
admin.site.register(PrakataKepalaSekolah)
admin.site.register(PrakataKepalaSekolahsmp)
admin.site.register(VisidanMisi)
admin.site.register(StrukturOrganisasi)


#Berita
admin.site.register(Berita)

#header
admin.site.register(Header)
admin.site.register(Footer)