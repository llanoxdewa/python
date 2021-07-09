from django import forms
from .models import Instagram

class FormInstagram(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = [
            'nama_depan',
            'nama_belakang',
            'username',
            'password',
            'email'
        ]

        labels = {
            'email' : 'Email Address',
            'nama_depan' : 'Nama depan',
            'nama_belakang' : 'Nama belakang'
        }

        widgets = {
            'password' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'nama_depan' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'nama_belakang' : forms.TextInput(
                attrs={
                    'class' : 'form-control'
                }
            )
        }









