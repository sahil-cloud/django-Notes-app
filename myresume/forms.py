from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ("title",'desc')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Add title'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Add description','rows':'4'})
        }
