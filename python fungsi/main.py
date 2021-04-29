def luas(panjang,lebar):
    panjang += 1
    print(f'panjang didalam fungsi adalah {panjang}')
    return panjang * lebar
    # print('luas :',panjang * lebar)

def main():
    panjang = int(input('masukan panjang :'))
    lebar = int(input('masukan lebar :'))
    # untuk membuktikan bahwa variabel panjang input dengan variabel panjang di dalam fungsi atau variabel sebagai parameter itu berbeda
    print('panjang input :',panjang)
    luas1 = luas(panjang,lebar)
    print(f'panjang setelah keluar fungsi {panjang}')
    panjang = int(input('masukan panjang :'))
    lebar = int(input('masukan lebar :'))
    print('panjang input :',panjang)
    luas2 = luas(panjang,lebar)
    print(f'panjang setelah keluar fungsi {panjang}')
    print(luas1 + luas2)

main()
