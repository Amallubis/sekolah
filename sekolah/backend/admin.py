from django.contrib import admin
from backend.models import Sejarah,PrakataKepalaSekolah,PrakataKepalaSekolahsmp,VisidanMisi,StrukturOrganisasi, Berita,Header, Footer,PrestasiSekolah, Kurikulum, Runningtext, Agenda
# Register your models here.


admin.site.register(Sejarah)
admin.site.register(PrakataKepalaSekolah)
admin.site.register(PrakataKepalaSekolahsmp)
admin.site.register(VisidanMisi)
admin.site.register(StrukturOrganisasi)

#prestasi
admin.site.register(PrestasiSekolah)
admin.site.register(Kurikulum)
#Berita
admin.site.register(Berita)
admin.site.register(Agenda)

#header
admin.site.register(Header)
admin.site.register(Runningtext)
admin.site.register(Footer)