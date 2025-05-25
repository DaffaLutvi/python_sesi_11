def hitung_harga_setelah_diskon(harga_asli, diskon):
    return harga_asli * (1 - diskon / 100)

def hitung_pajak(harga, tarif_pajak):
    return harga * (tarif_pajak / 100)

def hitung_total(harga, pajak):
    return harga + pajak
