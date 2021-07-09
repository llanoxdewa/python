from django import forms

class ContactForm(forms.Form):

    nama = forms.CharField(max_length=10,label="Nama Lengkap")
    username = forms.CharField(max_length=20)
    email = forms.EmailField(label="Alamat Email")
    gender = forms.ChoiceField(
        choices=(
            ("laki-laki","male"),
            ("perempuan","female")
        ),
        widget=forms.RadioSelect
    )
    tgl_lahir = forms.DateField(widget=forms.SelectDateWidget(years=range(2000,2022)))
    alamat = forms.CharField(
        required=False,
        widget = forms.Textarea
    )
