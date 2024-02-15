# Pastikan kamu sudah menginstal modul tabulate
from tabulate import tabulate


class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai


mahasiswa_list = []


def tambah():
    nama = input("\nMasukkan nama mahasiswa: ")
    nilai = input("Masukkan nilai mahasiswa: ")
    mahasiswa_list.append(Mahasiswa(nama, nilai))
    print("Data mahasiswa telah ditambahkan.")


def tampilkan():
    if not mahasiswa_list:
        print("\nBelum ada data mahasiswa.")
        return

    data = []
    for nomor, mahasiswa in enumerate(mahasiswa_list, start=1):
        data.append([nomor, mahasiswa.nama, mahasiswa.nilai])

    headers = ["No", "Nama Mahasiswa", "Nilai"]
    print(tabulate(data, headers=headers, tablefmt="grid"))


def hapus(nama):
    for mahasiswa in mahasiswa_list:
        if mahasiswa.nama == nama:
            mahasiswa_list.remove(mahasiswa)
            print(f"Data mahasiswa {nama} telah dihapus.")
            return
    print(f"Data mahasiswa {nama} tidak ditemukan.")


def ubah(nama):
    for mahasiswa in mahasiswa_list:
        if mahasiswa.nama == nama:
            nilai_baru = input("Masukkan nilai baru: ")
            mahasiswa.nilai = nilai_baru
            print(f"Data mahasiswa {nama} telah diubah.")
            return
    print(f"Data mahasiswa {nama} tidak ditemukan.")


while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar\n")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("\nMasukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("\nMasukkan nama mahasiswa yang akan diubah: ")
        ubah(nama)
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")
