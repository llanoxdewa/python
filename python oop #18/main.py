# diaomond problem

class A:
    def show(self):
        print("ini adalah class A")
  

class B(A):
    def show(self):
        print("ini adalah class B")
 

class C(A):
    def show(self):
        print("ini adalah class C")
    
class D(B,C):
    pass
# urutan nya adalah B-C-A jika B tidak ada maka akan mengambil C dan seterusnya

objek = D()
objek.show()

    