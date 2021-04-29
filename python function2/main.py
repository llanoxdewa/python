# param1 dan param2 merupakan formalparameter 
# a dan b pada myfunction merupakan actual parameter
class Person:
    nama = 'no nama'

def myfunction(person, bilangan):
    person = Person()
    person.nama = 'dodol'
    bilangan = 12
    print(person.nama)
    print(bilangan)

def main():
    p = Person()
    p.nama = 'joko'
    bilangan = 22
    myfunction(p,bilangan)
    print(p.nama)
    print(bilangan)
main()

#  fungsi dengan default parameter
def default(a = 3, b = 2, c = 12):
    print(a,b,c)
default(b = 4,a = 2, c = 11)