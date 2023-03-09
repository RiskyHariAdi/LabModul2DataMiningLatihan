import json


with open("Latihan4_2.json") as file:
    data = json.load(file)

for mahasiswa in data:
    print("Nama:", mahasiswa["nama"])
    print("NIM:", mahasiswa["nim"])
    print("Kelas:", mahasiswa["kelas"])
    print("Jurusan:", mahasiswa["jurusan"])
    print("Alamat:", mahasiswa["alamat"])
    print("Hobby:", ", ".join(mahasiswa["hobby"]))
    print()
