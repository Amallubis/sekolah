from django.forms import ModelForm
from beranda.models import Contact


class FormContact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

