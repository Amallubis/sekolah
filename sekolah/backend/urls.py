from django.urls import path
from backend import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sejarah/', views.sejarah, name='sejarah'),
    path('prakata/', views.prakata, name='prakata'),
    path('prakatasmp/', views.prakatasmp, name='prakatasmp'),
    path('visi/', views.visidanmisi, name='visi'),
    path('add-struktur/', views.add_struktur, name='add-struktur'),
    path('edit-struktur/<int:id_edit>/', views.edit_struktur, name='edit-struktur'),
    path('delet-struktur/<int:id_delete>/', views.delete_struktur, name='delete-struktur'),
    # Berita
    path('add-berita',views.add_berita, name='add-berita'),
    path('edit-berita/<int:id_edit>/',views.edit_berita, name='edit-berita'),
    path('delete-berita/<int:id_delete>/',views.delete_berita, name='delete-berita'),
    path('detail-berita',views.detail_berita, name='detail-berita'),

    #Setting
    path('edit-header',views.header, name='edit-header'),
    path('edit-footer',views.footer, name='edit-footer'),

    #contact
    path('contact/',views.contact, name='contact'),
    path('hapus-contact/<int:id_hapus>/',views.hapus, name='hapus-contact'),
    
    #prestasi Sekolah
    path('prestasi-sekolah/',views.prestasisekolah,name='prestasi-sekolah'),
    path('edit-prestasi/<int:id_edit>/',views.edit_prestasi,name='edit-prestasi'),
    path('delete-prestasi/<int:id_delete>/',views.delete_prestasi,name='delete-prestasi'),

    #kurikulum
    path('list-kurikulum/',views.list_kurikulum, name='list-kurikulum'),
    path('add-kurikulum/',views.add_kurikulum, name='add-kurikulum'),
    path('edit-kurikulum/<int:id_edit>/',views.edit_kurikulum, name='edit-kurikulum'),
    path('delete-kurikulum/<int:id_delete>/',views.delete_kurikulum, name='delete-kurikulum'),
    

]
