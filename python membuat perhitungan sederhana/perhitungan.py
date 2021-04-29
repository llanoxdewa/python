# latihan konversi satuan suhu

# program konversi suhu

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("masukan suhu dalam celcius :"))
print("suhu adalah", celcius ,"C")


# reamur (4/5)
reamur = (4/5) * celcius
print("suhu celcius dalam reamur adalah", reamur ,"R")

# farenhait
fahrenhait = ((9/5) * celcius) + 32
print("suhu di dalam fahrenhait adalah", fahrenhait, "F")

# kelvin
kelvin = celcius + 273
print("suhu di dalam kelvin adalah", kelvin, "F")

# masukan nilai farenhait
print("\n=========PR=========\n")
farenhait = float(input("masukan suhu :"))
print("suhu adalah :", farenhait, "F")

suhu_K = (((5/9) * farenhait) - 32) + 273
print("suhu dalam kelvin", suhu_K, "K")

# suhu dalam reamur
kelvin = float(input("masukan suhu :"))
print("suhu adalah :", kelvin, "K")

suhu_f = ((kelvin - 273) * (9/5))  + 32

print("suhu dalam Fahrenhait :", suhu_f, "F")





