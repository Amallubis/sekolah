from django.shortcuts import render, redirect
from django.contrib import messages
from backend.models import Sejarah, PrakataKepalaSekolah,VisidanMisi,StrukturOrganisasi,Berita
from backend.forms import FormSejarah, FormPrakata, FormVisidanMisi, FormStrukturOrganisasi, FormBerita

# Create your views here.

def dashboard(request):
    context ={
        'title':'Dashboard'
    }
    return render(request,'backend/dashboard.html',context)

    

#Profil

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
       

def struktur(request):
    struktur = StrukturOrganisasi.objects.all().order_by('-pk')
    context ={
        'title':'Struktur',
        'struktur':struktur
    }
    return render(request,'backend/add-struktur.html',context)

    
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
       
       
def delete_struktur(request,id_delete):
    struktur = StrukturOrganisasi.objects.get(id=id_delete)
    struktur.delete()
    messages.success(request,'Berhasil di Delete')
    return redirect('add-struktur')



#Berita 
def detail_berita(request):
    berita = Berita.objects.all() 
    return render(request,'backend/detail-berita.html',{'berita':berita})

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

def delete_berita(request,id_delete):
    berita = Berita.objects.get(id=id_delete) 
    berita.delete()
    return redirect('detail-berita')