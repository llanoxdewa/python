from django.shortcuts import render
teks = """
selamat datang di web berita kami silahkan baca berita yang ada
kami harap anda tidak bosa membaca berita yang kami sediakan di web kami ini
"""

def berita(req):
    data = {
        'judul':'page berita',
        'header':'selamat datang di page berita',
        'teks':teks
    }
    return render(req,'berita/index.html',data)

