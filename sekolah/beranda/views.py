from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage,Page,PageNotAnInteger
from backend.models import Berita, Footer, Header, Sejarah, PrakataKepalaSekolah, PrakataKepalaSekolahsmp, VisidanMisi, StrukturOrganisasi, PrestasiSekolah, Runningtext, Agenda, Kurikulum, ProgramKerja, Download, Video
from beranda.forms import FormContact

import datetime
# Create your views here.
def beranda(request):
    berita = Berita.objects.all().order_by('-pk')[0:6]
    prakata = PrakataKepalaSekolah.objects.get(pk=1)
    prakatasmp = PrakataKepalaSekolahsmp.objects.get(pk=1)
    agenda = Agenda.objects.all().order_by('-pk')[0:5]
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    now = datetime.datetime.now()
    running = Runningtext.objects.get(pk=1)
    video = Video.objects.all()
    
    context ={
        'title':'Sekolah Advent Lubuk Pakam',
        'waktu':now,
        'berita':berita,
        'prakata':prakata,
        'prakatasmp':prakatasmp,
        'running':running,
        'agenda':agenda,
        'header':header,
        'footer':footer,
        'video':video
    }
    return render(request,'beranda/beranda.html',context)


def beranda_sejarah(request):
    sejarah= Sejarah.objects.get(pk=1) 
    prakata = PrakataKepalaSekolah.objects.get(pk=1)
    prakatasmp = PrakataKepalaSekolahsmp.objects.get(pk=1)
    visidanmisi = VisidanMisi.objects.get(pk=1)
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
        'title':'Profil',
        'sejarah':sejarah,
        'prakata':prakata,
        'prakatasmp':prakatasmp,
        'visidanmisi':visidanmisi,
        'header':header,
        'footer':footer
    }
    return render(request,'beranda/beranda-sejarah.html',context)


def beranda_prakata(request):
    prakata= PrakataKepalaSekolah.objects.get(pk=1)
    prakatasmp= PrakataKepalaSekolahsmp.objects.get(pk=1)
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context = {
        'title':'Prakata',
        'prakata':prakata,
        'prakatasmp':prakatasmp,
        'header':header,
        'footer':footer,
    }
    return render(request,'beranda/beranda-prakata.html',context)

def beranda_visi(request):
    visi   = VisidanMisi.objects.get(pk=1)
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
        'title':'Visi dan Misi',
        'visi':visi,
        'header':header,
        'footer':footer,
    } 
    return render(request,'beranda/beranda-visi.html',context)

def beranda_struktur(request):
    struktur= StrukturOrganisasi.objects.all()
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
        'title':'Struktur Organisasi',
        'struktur':struktur,
        'header':header,
        'footer':footer,

    }
    return render(request,'beranda/beranda-struktur.html',context)

    
def beranda_berita(request, id_berita):
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    b= Berita.objects.get(id=id_berita)
    context ={
        'title':'Detail Berita',
        'berita':b,
        'header':header,
        'footer':footer,
    }
    return render(request,'beranda/beranda-berita.html',context)


def beranda_kurikulum(request):
    kurikulum = Kurikulum.objects.all().order_by('-pk')
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
        'title':'Kurikulum',
        'kurikulum':kurikulum,
        'header':header,
        'footer':footer,
    }
    return render(request,'beranda/beranda-kurikulum.html',context)

def beranda_contact(request):
    if request.POST:
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Pesan anda berhasil dikirim')
            form = FormContact()
            header = Header.objects.get(pk=1)
            footer = Footer.objects.get(pk=1)
            context ={
                'title':'Contact',
                'form':form,
                'header':header,
                'footer':footer
            }
            return render(request,'beranda/beranda-contact.html',context)
    else:
        form = FormContact()
        header = Header.objects.get(pk=1)
        footer = Footer.objects.get(pk=1)
        context ={
            'title':'Contact',
            'header':header,
            'footer':footer,
            'form':form
        }
        return render(request,'beranda/beranda-contact.html',context)
    
    
def programsekolah(request):
    programkerja = ProgramKerja.objects.all().order_by('-pk')
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
       'title':'Program Sekolah',
       'header':header,
       'footer':footer,
       'programkerja':programkerja
    }
    return render(request,'beranda/programsekolah.html',context)


def beranda_prestasi(request):
    prestasi = PrestasiSekolah.objects.all().order_by('-pk')
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
        'title':'Prestasi Sekolah',
        'header':header,
        'footer':footer,
        'prestasi':prestasi
    }
    return render(request,'beranda/beranda-prestasisekolah.html',context)



def beranda_beritaall(request):
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    berita = Berita.objects.all()
    beritas = Berita.objects.all()
    paginator = Paginator(beritas, 4)
    page = request.GET.get('page')

    try:
        berita = paginator.page(page)
    except EmptyPage:
        berita = paginator.page(paginator.num)
    except PageNotAnInteger:
        berita = paginator.page(1)
    context = {
        'title':'Berita',
        'header':header,
        'footer':footer,
        'berita':berita, 
    }
    return render(request,'beranda/beranda-beritaall.html',context)


def beranda_jadwal(request):
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    agenda = Agenda.objects.all().order_by('-pk')
    context ={
        'title':'Jadwal Kegiatan',
        'agenda':agenda,
        'header':header,
        'footer':footer,
    }
    return render(request,'beranda/beranda-jadwal.html',context)

def beranda_download(request):
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    download = Download.objects.all()
    context ={
        'title':'Download',
        'download':download,
        'header':header,
        'footer':footer
    }
    return render(request,'beranda/beranda-download.html',context)
def beranda_video(request):
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    video = Video.objects.all()
    context ={
        'title':'Download',
        'video':video,
        'header':header,
        'footer':footer
    }
    return render(request,'beranda/beranda-video.html',context)


def privacy(request):
    header = Header.objects.get(pk=1)
    footer = Footer.objects.get(pk=1)
    context ={
        'title':'Privacy Policy',
        'header':header,
        'footer':footer,
    }
    return render(request,'beranda/privacy.html',context)
    
