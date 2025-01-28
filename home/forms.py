from django import forms
from .models import Constituency

class ConstituencyForm(forms.ModelForm):
    class Meta:
        model = Constituency
        fields = ['name', 'district', 'khayine', 'township', 'file', 'detail_file']  # Add fields as required
