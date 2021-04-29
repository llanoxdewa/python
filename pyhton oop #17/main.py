# method resolution order // multiple inheritence

class A:
    def show(self):
        print('ini adalah show A')
        
class B:
    def show(self):
        print('ini adalah show B')
 

class C(A,B):
    pass
    
        
       
objek = C()
objek.show()
# help(objek)

