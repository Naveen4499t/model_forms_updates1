from django import forms
from app.models import *

class ModelForms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['Topic_name','url']
        #exclude=['url']
        help_texts={'Topic_name':'should not be interger','name':'only Alphabets'}
        labels={'Topic_name':'TN','name':'NA'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}


class AcessRecordsForms(forms.ModelForm):
    class Meta:
        model=Acessrecords
        fields='__all__'
   