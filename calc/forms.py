from django.forms import ModelForm, fields
from .models import Allgroups,Services, patient
class PostForm(ModelForm):
    class Meta:
        model=Allgroups
        fields="__all__"

class PostForm1(ModelForm):
    class Meta:
        model=Services
        fields="__all__"

class PostForm2(ModelForm):
    class Meta:
        model=patient
        fields="__all__"