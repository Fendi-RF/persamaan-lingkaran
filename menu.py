# import library
import math

# Class untuk nilai B dan C
class pers_kuadrat:
    def __init__(self, x):
        self.x = x
    def nilai_b(self):
        b = (self.x + self.x)* -1
        return b
    def nilai_c(self):
        c = self.x ** 2
        return c

# fungsi fungsi
def c_zero_twonum():
    print('Persamaan Lingkaran Titik (0, 0) jika diketahui titik yang dilewati')
    x = int(input('masukkan x: \n'))
    y = int(input('masukkan y: \n'))
    x = x**2
    y = y **2

    r = math.sqrt(x+y)
    print('r = ', r)
    r = r **2
    print('x^2 + y^2 = ', r)

def c_zero_onenum():
    print('Persamaan Lingkaran Titik (0, 0) jika diketahui jari-jarinya')
    r = int(input('masukkan r: \n'))
    
    r = r **2
    print('x^2 + y^2 = ', r)

def c_num_num():
    # (x - a)^2 + (y - b)^2 = r^2
    print('Persamaan Lingkaran Titik (x, y) jika diketahui jari-jarinya')
    x = pers_kuadrat(int(input('masukkan titik pusat x: \n')))
    y = pers_kuadrat(int(input('masukkan titik pusat y: \n')))
    r = int(input('masukkan r: \n'))

    print(f'x^2 + y^2 + {x.nilai_b()}x + {y.nilai_b()}y + {x.nilai_c() + y.nilai_c() - r **2} = 0')

def c_num_twonum():
    # (x - a)^2 + (y - b)^2 = r^2
    print('Persamaan Lingkaran Titik (x, y)) jika diketahui titik yang dilewati')
    x = int(input('masukkan titik pusat x: \n'))
    y = int(input('masukkan titik pusat y: \n'))
    a = int(input('masukkan titik yang dilewati a: \n'))
    b = int(input('masukkan titik yang dilewati b: \n'))

    r = math.sqrt((a - x)**2+(b - y)**2)

    x = pers_kuadrat(x)
    y = pers_kuadrat(y)

    print('r = ', r)
    print(f'x^2 + y^2 + {x.nilai_b()}x + {y.nilai_b()}y + {x.nilai_c() + y.nilai_c() - r **2} = 0')

def bupl():
    print('Bentuk Umum Persamaan Lingkaran')
    a = int(input('masukkan A (ex : 2ax): \n'))
    b = int(input('masukkan B (ex : 2ay): \n'))
    c = int(input('masukkan C (tanpa variabel): \n'))

    print(f'titik pusat = ({a/2*-1}, {b/2*-1})')

    r = math.sqrt((a/2*-1)**2+(b/2*-1)**2 - c)
    print('jari-jari =', r)


# Main Menu
def menu():
    print('+++++++++++++Persamaan Lingkaran+++++++++++++++++')
    print('Pilih menu :')
    print('1. Persamaan Lingkaran Titik (0, 0)')
    print('2. Persamaan Lingkaran Titik (x, y)')
    print('3. Bentuk Umum Persamaan Lingkaran')
    print('0. Keluar')
    input1 = int(input('Masukkan Pilihan: \n'))
    if input1 == 1:
        print('+++++++++++++Persamaan Lingkaran+++++++++++++++++')
        print('Pilih menu :')
        print('1. Persamaan Lingkaran Titik (0, 0) jika diketahui jari-jarinya')
        print('2. Persamaan Lingkaran Titik (0, 0) jika diketahui titik yang dilewati')
        print('0. Kembali ke menu')
        input2 = int(input('Masukkan Pilihan: '))
        if input2 == 1:
            c_zero_onenum()
        elif input2 == 2:
            c_zero_twonum()
        elif input2 == 0:
            menu()
        else:
            print('Menu yang dipilih salah!')
    elif input1 == 2:
        print('+++++++++++++Persamaan Lingkaran+++++++++++++++++')
        print('Pilih menu :')
        print('1. Persamaan Lingkaran Titik (x, y) jika diketahui jari-jarinya')
        print('2. Persamaan Lingkaran Titik (x, y)) jika diketahui titik yang dilewati')
        print('0. Kembali ke menu')
        input2 = int(input('Masukkan Pilihan: '))
        if input2 == 1:
            c_num_num()
        elif input2 == 2:
            c_num_twonum()
        elif input2 == 0:
            menu()
        else:
            print('Menu yang dipilih salah!')
    elif input1 == 3:
        bupl()
        # re = input('Ulangi Program (p), Kembali ke menu(m), Keluar(k)')
        # if re == 'p':
        #     bupl()
        # elif re == 'm':
        #     menu()
        # elif re == 'k':
        #     exit()

    elif input1 == 0:
        exit()
    else:
        print('Menu yang dipilih salah!')

# Main loop
if __name__ == "__main__":
  while(True):
    menu()
