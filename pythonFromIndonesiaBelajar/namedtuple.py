from collections import namedtuple
# gunakan fungsi _asdict() untuk merubah data menajadi tipe dict
# gunakan _replace() untuk menghapus komponen

# Data = namedtuple('dataSiswa',('nama','kelas','nilai'))
# siswa = Data(
#     nama={
#         1212:'llano',
#         2323:'ujang',
#         5252:'dadang'
#     },
#     kelas={
#         'llano':'11 elektro 1',
#         'ujang':'10 las 1',
#         'dadang':'12 kimia 2'
#     },
#     nilai={
#         'llano':100,
#         'ujang':90,
#         'dadang':60
#     }
# )

data_input = {
    'nama':[
        'llano',
        'ujang',
        'dadang'
    ],
    'kelas':{
        'llano':'XIE1',
        'ujang':'XIK2',
        'dadang':'XLAS3'
    }
}
Datab = namedtuple('data',('nama','kelas'))

siswa = Datab(**data_input)
