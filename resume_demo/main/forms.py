from django import forms
from .models import ContactProfile

# setting form with respect to model.py
# for templating
class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
                        widget=forms.TextInput(
                            attrs={
                                'placeholder': '*Full name..',
                            }
                        ))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={'placeholder': '*Email..'}))

    
    message = forms.CharField(max_length=1000 , required=True,
                        widget = forms.TextInput(attrs={
                            'placeholder':'*Email..',
                            'rows':6,
                        })    )
    
    class Meta:
        model = ContactProfile # defines that model form is associated with this model
        fields = ('name','email','message',)
