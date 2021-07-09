from django import forms
from .models import PostModel

# class PostForm(forms.Form):
#     judul = forms.CharField(max_length=20)
#     body = forms.CharField(widget=forms.Textarea)
#     category = forms.CharField(max_length=20)

#     def clean_judul(self):
#         judul_input = self.cleaned_data.get('judul')
#         if judul_input in [post.get('judul') for post in PostModel.objects.values('judul')]:
#             raise forms.ValidationError(f"{judul_input} sudah ada")
#         return judul_input

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'judul',
            'body',
            'category'
        ]

    def clean_body(self):
        SARKAS = ['babi','monyet','anjing','babi','tralala','ular']
        KATA_BERSIH = []
        text_body_input = self.cleaned_data.get('body',None)
        for kata in text_body_input.split(' '):
            if kata in SARKAS:
                KATA_BERSIH.append("*" * len(kata))
                continue
            KATA_BERSIH.append(kata)
        return ' '.join(KATA_BERSIH)


