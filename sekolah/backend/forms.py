from django.forms import ModelForm
from backend.models import Sejarah, PrakataKepalaSekolah,PrakataKepalaSekolahsmp, VisidanMisi, StrukturOrganisasi, Berita, Header, Footer, PrestasiSekolah, Kurikulum, Runningtext, Agenda

class FormSejarah(ModelForm):
    class Meta:
        model = Sejarah
        fields = '__all__'

        
class FormPrakata(ModelForm):
    class Meta:
        model = PrakataKepalaSekolah
        fields = '__all__'
class FormPrakatasmp(ModelForm):
    class Meta:
        model = PrakataKepalaSekolahsmp
        fields = '__all__'

        
class FormVisidanMisi(ModelForm):
    class Meta:
        model = VisidanMisi
        fields = '__all__'
        

class FormStrukturOrganisasi(ModelForm):
    class Meta:
        model = StrukturOrganisasi
        fields = '__all__'

        
class FormBerita(ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'


class FormHeader(ModelForm):
    class Meta:
        model = Header
        fields = '__all__'


class FormFooter(ModelForm):
    class Meta:
        model = Footer
        fields = '__all__'

        
class FormHeader(ModelForm):
    class Meta:
        model = Header
        fields = '__all__'

        
class FormPrestasiSekolah(ModelForm):
    class Meta:
        model = PrestasiSekolah
        fields = '__all__'
        
        
class FormKurikulum(ModelForm):
    class Meta:
        model = Kurikulum
        fields = '__all__'
        
        
        
class FormRunningtext(ModelForm):
    class Meta:
        model = Runningtext
        fields = '__all__'
        
class FormAgenda(ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'