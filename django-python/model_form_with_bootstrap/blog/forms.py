from django import forms

from .models import PostModel
# from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'author',
            'judul',
            'body',
            'category'
        ]
        labels = {
            'author' : 'penulis'
        }
        widgets = {
            'author' : forms.TextInput(
                attrs = {
                    'class' : "form-control",
                    'placeholder' : 'masukan nama author'
                }
            ),

            'judul' : forms.TextInput(
                attrs = {
                    'class' : "form-control",
                    'placeholder' : 'masukan judul artikel'
                }
            ),

            'body' : forms.Textarea(
                attrs = {
                    'class' : "form-control"
                }
            ),

            'category' : forms.Select(
                choices = (
                    ('gosip','Gosip'),
                    ('olahraga','Olahraga'),
                    ('berita','Berita')
                ),
                attrs = {
                    'class' : "form-control",
                }
            )
        }

    def clean_judul(self):
        judul_input = self.cleaned_data.get('judul',None)
        if judul_input in [post.get('judul',None) for post in PostModel.objects.values('judul')]:
            raise forms.ValidationError(f"{judul_input} sudah ada")
        return judul_input

    def clean_body(self):
        SARKAS = ("anjing","babi","setan","bangsat","kuda","curut","cebong","kampret","asu","demit","monyet")
        text_input = self.cleaned_data.get('body').split(' ')
        kata_bersih = []
        for kata in text_input:
            if kata.lower() in SARKAS:
                kata_bersih.append('*' * len(kata))
                continue
            kata_bersih.append(kata)
        return ' '.join(kata_bersih)


