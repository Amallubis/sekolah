from django.urls import path
from beranda import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('beranda-sejarah/', views.beranda_sejarah, name='beranda-sejarah'),
    path('beranda-prakata/', views.beranda_prakata, name='beranda-prakata'),
    path('beranda-visi/', views.beranda_visi, name='beranda-visi'),
    path('beranda-struktur/', views.beranda_struktur, name='beranda-struktur'),
    path('beranda-berita<int:id_berita>/', views.beranda_berita, name='beranda-berita'),
    path('beranda-kurikulum/', views.beranda_kurikulum, name='beranda-kurikulum'),
    path('beranda-contact/',views.beranda_contact, name='beranda-contact'),
    path('programsekolah/',views.programsekolah, name='programsekolah'),
    path('beranda-prestasi/',views.beranda_prestasi, name='beranda-prestasi'),
    path('beranda-beritaall/',views.beranda_beritaall, name='beranda-beritaall'),
]
