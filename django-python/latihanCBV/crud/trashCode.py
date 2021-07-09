# for showing data from model
# def index(request):
#     instagram_data = Instagram.objects.all()
#     return render(request,'sosmed/index.html',{
#         'title' : 'sosmed page | home ',
#         'instagram_data' : instagram_data,
#         'remove_data' : False
#     })

# for deete data
#def delete(request,user_delete):
#     Instagram.objects.filter(id=user_delete).delete()
#     return redirect("sosmed:index")

# def delete_page(request):
#     instagram_data = Instagram.objects.all()
#     return render(request,'sosmed/index.html',{
#         'title' : 'sosmed page | delete page',
#         'instagram_data' : instagram_data,
#         'remove_data' : True
#     })

















