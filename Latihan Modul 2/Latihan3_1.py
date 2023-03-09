Nama = ["Risky HariAdi", "Fatimah Az Zahra", "Budi Susanto"]

def hitung_vokal(string):
    vokal = "aiueoAIUEO"
    count = 0
    for char in string:
        if char in vokal:
            count += 1
    return count

for n in Nama:
    vokal_nama_depan = hitung_vokal(n.split()[0])
    vokal_nama_belakang = hitung_vokal(n.split()[1])
    print(f"Nama: {n}, Huruf vokal pada nama depan: {vokal_nama_depan}, Huruf vokal pada nama belakang: {vokal_nama_belakang}")
