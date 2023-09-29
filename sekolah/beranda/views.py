from django.shortcuts import render
import datetime
# Create your views here.
def beranda(request):
    now = datetime.datetime.now()
    context ={
        'title':'Sekolah Advent Lubuk Pakam',
        'waktu':now
    }
    return render(request,'beranda/beranda.html',context)