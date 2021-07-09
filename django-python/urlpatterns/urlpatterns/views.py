from django.http import HttpResponse

def respones(req,input=0):
    return HttpResponse(f"<h1>{input}</h1>")


# def tanggal(req,**data_input):
#     if(int(data_input['tanggal']) > 31):
#         return HttpResponse("<h1 style='color:red;'>tanggal tidak valid</h1>")
#     elif(int(data_input['bulan']) > 12):
#         return HttpResponse("<h1 style='color:red;'>bulan tidak valid</h1>")
#     return HttpResponse(f"<h1>{data_input['tanggal']}/{data_input['bulan']}/{data_input['tahun']}</h1>")











