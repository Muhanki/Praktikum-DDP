# Fungsi untuk menghitung luas dan keliling persegi
def hitung_persegi(sisi):
    # Menghitung luas dan keliling
    luas = sisi ** 2
    keliling = 4 * sisi
    return luas, keliling

# # Input sisi persegi dari pengguna
sisi = float(input("Masukkan panjang sisi persegi: "))

# # Menghitung luas dan keliling
luas, keliling = hitung_persegi(sisi)

# # Menampilkan hasil
print(f"Luas Persegi: {luas}")
print(f"Keliling Persegi: {keliling}")

# # menghitung luas segitiga
def hitung_segitiga (tinggi):
    alas = float(input("masukkan alas segitiga: "))
    tinggi = float(input("masukkan tinggi segitiga: "))

    luas = (float(alas * tinggi) / 2)             
print ('luas segitiga adalah : ',luas)

# mencari luas lingkaran
def hitung_lingkaran(r):

    r = float(input("Masukkan jari-jari: "))

    phi = 3.14
    diameter = 2*r

    luas = phi *    r*r
    keliling = phi * diameter

print('\nluasnya  =',  str("%.2f" % luas))
print('kelilingnya  =',  str("%.2f" % keliling))
# luas, keliling = hitung_lingkaran(jari_jari)
# print(f"Luas Lingkaran: {luas:.2f}")
# print(f"Keliling Lingkaran: {keliling:.2f}")

# menghitung luas lingkaran

# Fungsi untuk menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Input dari pengguna
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Menghitung luas
luas = hitung_luas_persegi_panjang(panjang, lebar) # type: ignore

# Menampilkan hasil
print(f"Luas persegi panjang adalah {luas}")


# menghitung luas jajar genjang

# Fungsi untuk menghitung luas jajar genjang
def hitung_luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

# Input dari pengguna
alas = float(input("Masukkan panjang alas: "))
tinggi = float(input("Masukkan tinggi: "))

# Menghitung luas
luas = hitung_luas_jajar_genjang(alas, tinggi)

# Menampilkan hasil
print(f"Luas jajar genjang adalah {luas}")


