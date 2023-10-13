from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import Sejarah, PrakataKepalaSekolah,PrakataKepalaSekolahsmp,VisidanMisi,StrukturOrganisasi,Berita, Footer, Header, PrestasiSekolah, Kurikulum, Runningtext, Agenda, ProgramKerja, Download, Video
from backend.forms import FormSejarah, FormPrakata,FormPrakatasmp, FormVisidanMisi, FormStrukturOrganisasi, FormBerita, FormFooter,FormHeader, FormPrestasiSekolah, FormKurikulum, FormRunningtext,FormAgenda, FormProgramKerja, FormDownload, FormVideo
from beranda.models import Contact
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    berita = Berita.objects.count()
    contact = Contact.objects.count()
    context ={
        'title':'Dashboard',
        'berita':berita,
        'contact':contact
        
    }
    return render(request,'backend/dashboard.html',context)

    

#Profil

@login_required(login_url=settings.LOGIN_URL)
def sejarah(request):
    if request.POST:
        sejarah = Sejarah.objects.get(pk=1)
        form = FormSejarah(request.POST, request.FILES, instance=sejarah)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            sejarah = Sejarah.objects.get(pk=1)
            form = FormSejarah(instance=sejarah)
            return render(request,'backend/sejarah.html',{'form':form})
    else:
        sejarah = Sejarah.objects.get(pk=1)
        form = FormSejarah(instance=sejarah)
        return render(request,'backend/sejarah.html',{'form':form, 'sejarah':sejarah})
   
   
@login_required(login_url=settings.LOGIN_URL)
def prakata(request):
    if request.POST:
        prakata = PrakataKepalaSekolah.objects.get(pk=1) 
        form = FormPrakata(request.POST, request.FILES, instance=prakata)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            return render(request,'backend/prakata.html',{'form':form,'prakata':prakata})
    else:
        prakata = PrakataKepalaSekolah.objects.get(pk=1)
        form = FormPrakata(instance=prakata)
        return render(request,'backend/prakata.html',{'form':form,'prakata':prakata}) 
def prakatasmp(request):
    if request.POST:
        prakatasmp = PrakataKepalaSekolahsmp.objects.get(pk=1) 
        form = FormPrakatasmp(request.POST, request.FILES, instance=prakatasmp)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            return render(request,'backend/prakatasmp.html',{'form':form,'prakatasmp':prakatasmp})
    else:
        prakatasmp = PrakataKepalaSekolahsmp.objects.get(pk=1)
        form = FormPrakata(instance=prakatasmp)
        return render(request,'backend/prakatasmp.html',{'form':form,'prakatasmp':prakatasmp}) 


@login_required(login_url=settings.LOGIN_URL)
def visidanmisi(request):
    if request.POST:
        visi= VisidanMisi.objects.get(pk=1)
        form = FormVisidanMisi(request.POST, request.FILES, instance=visi)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            visi = VisidanMisi.objects.get(pk=1)
            form = FormVisidanMisi(instance=visi)
            return render(request,'backend/visidanmisi.html',{'form':form,'visi':visi})
    else:
        visi = VisidanMisi.objects.get(pk=1)
        form = FormVisidanMisi(instance=visi)
        return render(request,'backend/visidanmisi.html',{'form':form, 'visi':visi})
       

@login_required(login_url=settings.LOGIN_URL)
def struktur(request):
    struktur = StrukturOrganisasi.objects.all().order_by('-pk')
    context ={
        'title':'Struktur',
        'struktur':struktur
    }
    return render(request,'backend/add-struktur.html',context)

    
@login_required(login_url=settings.LOGIN_URL)
def add_struktur(request):
    if request.POST:
        form = FormStrukturOrganisasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil ditambahkan')
            form = FormStrukturOrganisasi()
            struktur = StrukturOrganisasi.objects.all()
            return render(request,'backend/add-struktur.html',{'form':form, 'struktur':struktur})
    else:
        struktur = StrukturOrganisasi.objects.all()
        form = FormStrukturOrganisasi()
        return render(request,'backend/add-struktur.html',{'form':form, 'struktur':struktur})

        
@login_required(login_url=settings.LOGIN_URL)
def edit_struktur(request,id_edit):
    if request.POST:
        struktur = StrukturOrganisasi.objects.get(id=id_edit)
        form = FormStrukturOrganisasi(request.POST,request.FILES,instance=struktur)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            struktur = StrukturOrganisasi.objects.get(id=id_edit)
            form = FormStrukturOrganisasi(instance=struktur)
            return render(request,'backend/edit-struktur.html',{'form':form, 'struktur':struktur})
    else:
        struktur= StrukturOrganisasi.objects.get(id=id_edit)
        form = FormStrukturOrganisasi(instance=struktur)
        return render(request,'backend/edit-struktur.html',{'form':form,'struktur':struktur})
       
       
@login_required(login_url=settings.LOGIN_URL)
def delete_struktur(request,id_delete):
    struktur = StrukturOrganisasi.objects.get(id=id_delete)
    struktur.delete()
    messages.success(request,'Berhasil di Delete')
    return redirect('add-struktur')



#Berita 
@login_required(login_url=settings.LOGIN_URL)
def detail_berita(request):
    berita = Berita.objects.all() 
    return render(request,'backend/detail-berita.html',{'berita':berita})

@login_required(login_url=settings.LOGIN_URL)
def add_berita(request):
    if request.POST:
        form = FormBerita(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil menambahkan Berita')
            form = FormBerita()
            return render(request,'backend/add-berita.html',{'form':form})
    else:
        form = FormBerita()
        return render(request,'backend/add-berita.html',{'form':form})

@login_required(login_url=settings.LOGIN_URL)
def edit_berita(request,id_edit):
    if request.POST:
        berita = Berita.objects.get(id=id_edit)
        form = FormBerita(request.POST, request.FILES, instance=berita)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            berita = Berita.objects.get(id=id_edit)
            form = FormBerita(instance=berita)
            return render(request,'backend/edit-berita.html',{'form':form,'berita':berita})
    else:
        berita = Berita.objects.get(id=id_edit)
        form = FormBerita(instance=berita)
        return render(request,'backend/edit-berita.html',{'form':form,'berita':berita})

@login_required(login_url=settings.LOGIN_URL)
def delete_berita(request,id_delete):
    berita = Berita.objects.get(id=id_delete) 
    berita.delete()
    return redirect('detail-berita')



#Settingan

@login_required(login_url=settings.LOGIN_URL)
def header(request):
    if request.POST:
        header = Header.objects.get(pk=1)
        form = FormHeader(request.POST, request.FILES, instance=header)
        if form.is_valid():
            form.save()
            messages.success(request,'Header berhasil diubah') 
            header = Header.objects.get(pk=1)
            form = FormHeader(instance=header)
            header = Header.objects.get(pk=1)
            return render(request, 'backend/edit-header.html',{'form':form,'header':header})
    else:
        header = Header.objects.get(pk=1)
        form = FormHeader(instance=header)
        return render(request,'backend/edit-header.html',{'form':form, 'header':header})
        


@login_required(login_url=settings.LOGIN_URL)
def footer(request):
    if request.POST:
        footer = Footer.objects.get(pk=1)
        form = FormFooter(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            footer = Footer.objects.get(pk=1)
            form = FormFooter(instance=footer)
            return render(request,'backend/edit-footer.html',{'form':form,'footer':footer })
    else:
        footer = Footer.objects.get(pk=1)
        form = FormFooter(instance=footer)
        return render(request,'backend/edit-footer.html',{'form':form,'footer':footer})
    
    
    
@login_required(login_url=settings.LOGIN_URL)
def contact(request):
    contact = Contact.objects.all()
    context ={
        'title':'Contact',
        'contact':contact
    }
    return render(request,'backend/contact.html',context) 

@login_required(login_url=settings.LOGIN_URL)
def hapus(request,id_hapus):
    contact = Contact.objects.get(id=id_hapus)
    contact.delete()
    return redirect('contact')


#PRestasi Sekolah

@login_required(login_url=settings.LOGIN_URL)
def prestasisekolah(request):
    if request.POST:
        form = FormPrestasiSekolah(request.POST)
        if form.is_valid():
            form.save()
            form = FormPrestasiSekolah()
            prestasi = PrestasiSekolah.objects.all()
            messages.success(request,'Berhasil menambahkan Prestasi')
            return render(request,'backend/prestasisekolah.html',{'form':form,'prestasi':prestasi})
    else:
        form = FormPrestasiSekolah()
        prestasi = PrestasiSekolah.objects.all()
        return render(request,'backend/prestasisekolah.html',{'form':form,'prestasi':prestasi})

@login_required(login_url=settings.LOGIN_URL)
def edit_prestasi(request,id_edit):
    if request.POST:
        p= PrestasiSekolah.objects.get(id=id_edit)
        form = FormPrestasiSekolah(request.POST, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            p=PrestasiSekolah.objects.get(id=id_edit)
            form = FormPrestasiSekolah(instance=p)
            return render(request,'backend/editprestasi.html',{'form':form,'p':p})

    else:
        p= PrestasiSekolah.objects.get(id=id_edit)
        form = FormPrestasiSekolah(instance=p)
        return render(request,'backend/editprestasi.html',{'form':form,'p':p})



@login_required(login_url=settings.LOGIN_URL)
def delete_prestasi(request,id_delete):
    p = PrestasiSekolah.objects.get(id = id_delete)
    p.delete()
    return redirect('prestasi-sekolah')


@login_required(login_url=settings.LOGIN_URL)
def list_kurikulum(request):
    kurikulum = Kurikulum.objects.all()
    context ={
        'title':'Kurikulum',
        'kurikulum':kurikulum
    }
    return render(request,'backend/list-kurikulum.html',context)

@login_required(login_url=settings.LOGIN_URL)
def add_kurikulum(request):
    if request.POST:
        form = FormKurikulum(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request,'Kurikulum Berhasil ditambahkan')
            form = FormKurikulum()
            return render(request,'backend/add-kurikulum.html',{'form':form})
    else:
        form = FormKurikulum()
        return render(request,'backend/add-kurikulum.html',{'form':form}) 
    
@login_required(login_url=settings.LOGIN_URL)
def edit_kurikulum(request,id_edit):
    if request.POST:
        k = Kurikulum.objects.get(id=id_edit)
        form = FormKurikulum(request.POST, instance=k)
        if form.is_valid():
            form.save()
            messages.success(request,"Berhasil diupdate")
            k = Kurikulum.objects.get(id=id_edit)
            form = FormKurikulum(instance=k)
            return render(request,'backend/edit-kurikulum.html',{'form':form, 'k':k})
    else:
        k = Kurikulum.objects.get(id=id_edit)
        form =FormKurikulum(instance=k)
        return render(request,'backend/edit-kurikulum.html',{'form':form,'k':k})
    
@login_required(login_url=settings.LOGIN_URL)
def delete_kurikulum(request,id_delete):
    k = Kurikulum.objects.get(id=id_delete)
    k.delete()
    return redirect('list-kurikulum')

@login_required(login_url=settings.LOGIN_URL)
def runningtext(request):
    if request.POST:
        running = Runningtext.objects.get(pk=1)
        form = FormRunningtext(request.POST, instance=running)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            form = FormRunningtext(instance=running)
            return render(request,'backend/running-text.html',{'form':form})
    else:
        running = Runningtext.objects.get(pk=1)
        form = FormRunningtext(instance=running)
        return render(request,'backend/running-text.html',{'form':form})

@login_required(login_url=settings.LOGIN_URL)   
def agenda(request):
    if request.POST:
        form = FormAgenda(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil menambahkan Agenda')
            form = FormAgenda()
            agenda = Agenda.objects.all()
            return render(request,'backend/agenda.html',{'form':form, 'agenda':agenda})
    else:
        form = FormAgenda()
        agenda = Agenda.objects.all()
        return render(request,'backend/agenda.html',{'form':form,'agenda':agenda})
    
@login_required(login_url=settings.LOGIN_URL)   
def edit_agenda(request,id_edit):
    if request.POST:
        agenda = Agenda.objects.get(id=id_edit)
        form = FormAgenda(request.POST, instance=agenda) 
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            form = FormAgenda(instance=agenda)
            return render(request,'backend/edit-agenda.html',{'form':form,'agenda':agenda})
    else:
        agenda = Agenda.objects.get(id=id_edit)
        form = FormAgenda(instance=agenda)
        return render(request,'backend/edit-agenda.html',{'form':form,'agenda':agenda})

        
@login_required(login_url=settings.LOGIN_URL)   
def delete_agenda(request,id_delete):
    agenda = Agenda.objects.get(id=id_delete)
    agenda.delete()
    return redirect('agenda')


@login_required(login_url=settings.LOGIN_URL)   
def addprogramkerja(request):
    programkerja = ProgramKerja.objects.all().order_by('-pk')
    if request.POST:
        form = FormProgramKerja(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil menambahkan Program Kerja')
            programkerja=ProgramKerja.objects.all()
            form = FormProgramKerja()
            return render(request,'backend/add-programkerja.html',{'form':form,'programkerja':programkerja})

    else:
        programkerja=ProgramKerja.objects.all().order_by('-pk')
        form = FormProgramKerja()
        return render(request,'backend/add-programkerja.html',{'form':form,'programkerja':programkerja})
        
        

@login_required(login_url=settings.LOGIN_URL)   
def editprogramkerja(request,id_edit):
    if request.POST:
        programkerja = ProgramKerja.objects.get(id = id_edit)
        form = FormProgramKerja(request.POST, instance=programkerja)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil di update')
            programkerja = ProgramKerja.objects.get(id=id_edit)
            form = FormProgramKerja(instance=programkerja)
            return render(request,'backend/edit-programkerja.html',{'form':form,'programkerja':programkerja})
    else:
        programkerja = ProgramKerja.objects.get(id=id_edit)
        form = FormProgramKerja(instance=programkerja)
        return render(request,'backend/edit-programkerja.html',{'form':form,'programkerja':programkerja})

        
@login_required(login_url=settings.LOGIN_URL)   
def delete_programkerja(request,id_delete):
    programkerja = ProgramKerja.objects.get(id=id_delete)
    programkerja.delete()
    return redirect('add-programkerja')


@login_required(login_url=settings.LOGIN_URL)
def download(request):
    if request.POST:
        form = FormDownload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil upload files')
            download = Download.objects.all()
            return render(request,'backend/download.html',{'form':form, 'download':download})
    else:
        download = Download.objects.all()
        form = FormDownload()
        return render(request,'backend/download.html',{'form':form,'download':download})
    
    
def download_edit(request, id_edit):
    if request.POST:
        download = Download.objects.get(id=id_edit)
        form = FormDownload(request.POST, request.FILES, instance=download)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil diupdate')
            download = Download.objects.get(id=id_edit)
            return render(request,'backend/download-edit.html',{'form':form,'download':download})
    else:
        download = Download.objects.get(id=id_edit)
        form = FormDownload(instance=download)
        return render(request,'backend/download-edit.html',{'form':form,'download':download})
    
@login_required(login_url=settings.LOGIN_URL)
def download_delete(request,id_delete):
    download = Download.objects.get(id = id_delete)
    download.delete()
    return redirect('download')

@login_required(login_url=settings.LOGIN_URL)
def video(request):
    if request.POST:
        form = FormVideo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil Upload Video')
            video = Video.objects.all()
            form = FormVideo()
            return render(request,'backend/video.html',{'form':form,'video':video})
    else:
        form = FormVideo() 
        video = Video.objects.all()
        return render(request,'backend/video.html',{'form':form,'video':video})
@login_required(login_url=settings.LOGIN_URL)
def video_delete(request,id_delete):
    video= Video.objects.get(id = id_delete)
    video.delete()
    return redirect('video')