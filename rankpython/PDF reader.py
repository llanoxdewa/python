# oke gais kali ini kita akan membuat program untuk membaca file pdf
# kali ini akan sangat seru gais oke
# jangan lupa like and subrek channel saya ya gais
# jadi gasi kita akan menghitung luas karakter yang di block
import string

no_kata = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
alfabet = list(chr(i) for i in range(ord('a'),ord('z')+1))
#no_kata_alfabet = {a:k for (a,k) in zip(alfabet,no_kata)}
# pakai string
no_kata_alfabet = {a:k for (a,k) in zip(string.ascii_lowercase,no_kata)}
huruf = ['a','b','c']

# cara paten kali sluuuuur
def block(huruf,no_kata_alfabet):
	luas_block = len(huruf)*max([no_kata_alfabet[i] for i in huruf])
	return luas_block
print(block(huruf,no_kata_alfabet))












