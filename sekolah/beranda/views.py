from django.shortcuts import render
from backend.models import Berita
import datetime
# Create your views here.
def beranda(request):
    berita = Berita.objects.all().order_by('-pk')[0:6]
    now = datetime.datetime.now()
    context ={
        'title':'Sekolah Advent Lubuk Pakam',
        'waktu':now,
        'berita':berita
    }
    return render(request,'beranda/beranda.html',context)