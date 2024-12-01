# import math

# Fungsi untuk menghitung luas permukaan kubus
import math


def hitung_luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)

# Input dari pengguna
sisi = float(input("Masukkan panjang sisi kubus: "))

# Menghitung luas permukaan
luas_permukaan = hitung_luas_permukaan_kubus(sisi)

# Menampilkan hasil
print(f"Luas permukaan kubus adalah {luas_permukaan}")



# Fungsi untuk menghitung luas permukaan balok
def hitung_luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Input dari pengguna
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

# Menghitung luas permukaan
luas_permukaan = hitung_luas_permukaan_balok(panjang, lebar, tinggi)

# Menampilkan hasil
print(f"Luas permukaan balok adalah {luas_permukaan}")



# Fungsi untuk menghitung luas permukaan tabung
def hitung_luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

# Menghitung luas permukaan
luas_permukaan = hitung_luas_permukaan_tabung(jari_jari, tinggi)

# Menampilkan hasil
print(f"Luas permukaan tabung adalah {luas_permukaan:.2f}")


# Fungsi untuk menghitung luas permukaan limas segiempat
def hitung_luas_permukaan_limas(alas, tinggi_sisi):
    # Luas alas (persegi)
    luas_alas = alas ** 2
    # Luas seluruh sisi tegak (4 buah segitiga)
    luas_sisi = 4 * (0.5 * alas * tinggi_sisi)
    # Total luas permukaan
    return luas_alas + luas_sisi

# Input dari pengguna
alas = float(input("Masukkan panjang sisi alas (persegi): "))
tinggi_sisi = float(input("Masukkan tinggi sisi tegak: "))

# Menghitung luas permukaan
luas_permukaan = hitung_luas_permukaan_limas(alas, tinggi_sisi)

# Menampilkan hasil
print(f"Luas permukaan limas segiempat adalah {luas_permukaan:.2f}")

# Fungsi untuk menghitung luas permukaan prisma segitiga
def hitung_luas_permukaan_prisma(alas, tinggi_alas, tinggi_prisma, sisi_miring):
    # Luas dua alas (segitiga)
    luas_alas = 2 * (0.5 * alas * tinggi_alas)
    # Luas selimut (keliling alas dikalikan tinggi prisma)
    keliling_alas = alas + tinggi_alas + sisi_miring
    luas_selimut = keliling_alas * tinggi_prisma
    # Total luas permukaan
    return luas_alas + luas_selimut

# Input dari pengguna
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_alas = float(input("Masukkan tinggi alas segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))
sisi_miring = float(input("Masukkan panjang sisi miring segitiga: "))

# Menghitung luas permukaan
luas_permukaan = hitung_luas_permukaan_prisma(alas, tinggi_alas, tinggi_prisma, sisi_miring)

# Menampilkan hasil
print(f"Luas permukaan prisma segitiga adalah {luas_permukaan:.2f}")
