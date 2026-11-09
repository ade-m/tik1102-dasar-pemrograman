def pinjam(stok, kode, jumlah):
    if kode not in stok:
        return "Kode tidak dikenal"
    if jumlah <= 0:
        return "Jumlah tidak valid"
    if jumlah > stok[kode]:
        return "Stok tidak cukup"
    stok[kode] -= jumlah
    return "Berhasil"
