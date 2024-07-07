from django import forms
from django.core.validators import ValidationError
from . models import Message

class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=10, label="your name")
    name = forms.CharField(max_length=10, label="your text")
    
    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same', code='name_text')

    def clean_name(self):    
        name = self.cleaned_data.get('name')
        
        if ',' in name:
            raise ValidationError('dont use . , - in your name!' , code='syntaxt')
        return name
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widget ={
            "title":forms.TextInput(attrs={
                "class": "form-control",
                "placeholder":"enter your title",
                
            })
            
        }
            