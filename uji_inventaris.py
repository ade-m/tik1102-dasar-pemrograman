from inventaris import pinjam

kasus = [
    ("B01", 2, "Berhasil", 3),
    ("B01", 5, "Berhasil", 0),
    ("B01", 6, "Stok tidak cukup", 5),
    ("B01", 0, "Jumlah tidak valid", 5),
    ("B01", -1, "Jumlah tidak valid", 5),
    ("X01", 1, "Kode tidak dikenal", 5),
]
for kode, jumlah, status, sisa in kasus:
    stok = {"B01": 5}
    aktual = pinjam(stok, kode, jumlah)
    assert (aktual, stok["B01"]) == (status, sisa)
print("6 pengujian lulus")
