from django import forms

from msbdev.models import ContactForm


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['email', 'note']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm',
                                             'placeholder': 'Your email address'}),
            'note': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': '2',
                                          'placeholder': 'Leave a note'}),
        }
