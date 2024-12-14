class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Angkatan: {self.angkatan}")

if  __name__ == "__main__":
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan Tahun Angkatanmu: ")

    mahasiswa = Mahasiswa(nama, nim, angkatan)

    print("\nBiodata Mahasiswa:")
    mahasiswa.tampilkan_biodata()

    print(f"\nTotal Mahasiswa: {Mahasiswa.total_mahasiswa}")