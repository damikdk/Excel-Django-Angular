from django.forms import ModelForm
from .models import OfficeFile

class OfficeFileForm(ModelForm):
    class Meta:
        model = OfficeFile
        fields = ['file','dict_coor',]