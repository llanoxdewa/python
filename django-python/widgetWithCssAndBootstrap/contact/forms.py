from django import forms

class ContactForm(forms.Form):
    nama = forms.CharField(
        label="Nama Lengkap",
        max_length=20,
        widget=forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'masukan nama lengkap anda'
            }
        )
    )
    umur = forms.IntegerField(label="masukan umur")
    gender = forms.ChoiceField(
        label="jenis kelamin",
        choices=[
            ("laki-laki","male"),
            ('perempuan','female')
        ],
        widget=forms.RadioSelect

    )
    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1945,2006),
            attrs={
                'class' : 'form-control col-sm-2'
            }
        )
    )
    alamat = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs = {
                'class' : 'form-control is-valid'
            }
        )
    )
