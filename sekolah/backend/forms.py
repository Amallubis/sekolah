from django.forms import ModelForm
from backend.models import Sejarah, PrakataKepalaSekolah, VisidanMisi, StrukturOrganisasi, Berita

class FormSejarah(ModelForm):
    class Meta:
        model = Sejarah
        fields = '__all__'

        
class FormPrakata(ModelForm):
    class Meta:
        model = PrakataKepalaSekolah
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