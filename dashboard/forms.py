from django.forms import ModelForm, Form
import django.forms as f

class SearchForm(f.Form):
    search = f.CharField(widget=f.TextInput(attrs={'placeholder':'Search for...','class':'form-control'}))
    price = f.CharField(widget=f.TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}))
    option_list = [(1,'<') ,(2,'>'), (3,'=')]
    option = f.ChoiceField(choices=option_list)