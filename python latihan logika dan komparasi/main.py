# ------0+++++++5------8++++++++11--------

inAngka = int(input("masukan angka > 0 dan angka < 5 :"))

# > 0
lebih1 = inAngka > 0
print(inAngka, "lebih dari 0 =", lebih1)

# < 5
kurang1 = inAngka < 5
print(inAngka, "kurang dari 5 =", kurang1)

# irisan
incorrect = lebih1 and kurang1
print("angka yg anda masukan", incorrect)

print("\n",10*"=","\n")
inAngka = int(input("masukan angka > 8 dan angka < 11 :"))

# > 8
lebih = inAngka > 8
print(inAngka, "lebih dari 8 =", lebih)

# < 11
kurang = inAngka < 11
print(inAngka, "kurang dari 11 =", kurang)

incoorect1 = lebih and kurang 
print("angka yg anda masukan", incoorect1)


# membuat gabungan daerah rentang dari angka

# ++++++++3------------10+++++++++ 

inputUser = int(input("masukan angka yang < 3 atau angka > 10 :"))

# +++++++++3---------------
# memeriksa angka kurang dari 3
Kurangdari = inputUser < 3
print(inputUser,"kurang dari 3 =", Kurangdari)

# ---------10++++++++++++
lebihDari = inputUser > 10
print(inputUser,"lebih dari 10 =", lebihDari)

isCorrect = Kurangdari or lebihDari
print("angka yang anda masukan =", isCorrect)

#---------3++++++++++10-------------
# kasus irisan
inputUser1 = int(input("masukan angka yang > 3 dan angka < 10 :"))

# -------3++++++++++
lebih = inputUser1 > 3
print(inputUser1, "lebih dari 3", lebih)

# --------10+++++++++++
kurang = inputUser1 < 10
print(inputUser1,"kurang dari 10", kurang)

#---------3++++++++++10-------------
iscorrect = lebih and kurang 
print("angka anda =", iscorrect)




