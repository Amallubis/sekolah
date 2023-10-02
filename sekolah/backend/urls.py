from django.urls import path
from backend import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sejarah/', views.sejarah, name='sejarah'),
    path('prakata/', views.prakata, name='prakata'),
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
    

]
