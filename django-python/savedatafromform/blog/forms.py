from django import forms
from .models import PostModel

class PostForm(forms.Form):

    judul = forms.CharField(
        label="Judul",
        widget=forms.TextInput
    )

    body = forms.CharField(
        label="isi postingan",
        widget=forms.Textarea(attrs={
                'placeholder' : 'body'
        })
    )
    category = forms.CharField()

    email = forms.CharField(
        label="Email Address",
        widget=forms.EmailInput
    )
    # def clean_<nama row>
    def clean_judul(self):
        judul_input = self.cleaned_data.get('judul')
        if judul_input in [post.get('judul') for post in PostModel.objects.values('judul')]:
            raise forms.ValidationError(f"{judul_input} tidak boleh dijadikan judul karena sudah ada")
        return judul_input

    def clean_category(self):
        category_input = self.cleaned_data.get('category')
        if category_input.lower() not in [
            'berita','olahraga','jurnal','horor',
            'misteri','hot news','gosip','gaming'
        ]:
            raise forms.ValidationError(f"catetgory {category_input} tidak valid")

        return category_input



