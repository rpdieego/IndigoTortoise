from django import forms
from .models import ArticlesDb

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = ArticlesDb
        fields = ['shortname', 'title','link', 'category']
