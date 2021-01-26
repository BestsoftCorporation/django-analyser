from django.forms import ModelForm, Form
import django.forms as f

class SearchForm(f.Form):
    search = f.CharField(widget=f.TextInput(attrs={'placeholder':'Search for...','class':'form-control'}))