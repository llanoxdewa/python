from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class' : 'form-control'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class' : 'form-control'
        })
    )

    email_address = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'class' : 'form-control',
            'aria-describedby' : "emailHelp"
        }
    ))



