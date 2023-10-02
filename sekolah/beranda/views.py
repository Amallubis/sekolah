from django.shortcuts import render
from backend.models import Berita, Footer, Header
import datetime
# Create your views here.
def beranda(request):
    berita = Berita.objects.all().order_by('-pk')[0:6]
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    now = datetime.datetime.now()
    context ={
        'title':'Sekolah Advent Lubuk Pakam',
        'waktu':now,
        'berita':berita,
        'header':header,
        'footer':footer
    }
    return render(request,'beranda/beranda.html',context)