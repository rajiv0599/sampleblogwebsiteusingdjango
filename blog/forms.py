from django import forms
from .models import blogcomments
class newcommentform(forms.ModelForm):
    class Meta:
        model = blogcomments
        fields =['comment']