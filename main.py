"""
UTS Dasar Komputer dan Pemrograman
Kelompok B - Telekomunikasi: Monitoring Kualitas Sinyal / SNR
Nama: Bagas Ahmad Dita
NIM : 03041382631129

Jalankan dengan: python main.py
"""

# 15 data inti dari soal + 5 data tambahan untuk pengujian batas/variasi.
data_snr = [
    5, 8, 11, 14, 18, 22, 27, 9, 16, 24,
    12, 30, 7, 20, 15,
    9, 10, 19, 20, 35
]


def kualitas_sinyal(snr):
    """Menentukan kategori kualitas sinyal berdasarkan nilai SNR (dB)."""
    if snr < 10:
        return "RENDAH"
    elif snr < 20:
        return "BAIK"
    else:
        return "SANGAT BAIK"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori."""
    jumlah = {"RENDAH": 0, "BAIK": 0, "SANGAT BAIK": 0}
    for snr in data:
        status = kualitas_sinyal(snr)
        jumlah[status] += 1
    return jumlah


def statistik(data):
    """Menghitung rata-rata, nilai maksimum, dan minimum."""
    return sum(data) / len(data), max(data), min(data)


def tampilkan_hasil(data):
    """Menampilkan hasil klasifikasi setiap data dan ringkasan."""
    print("=" * 58)
    print("MONITORING KUALITAS SINYAL / SNR - KELOMPOK B")
    print("=" * 58)
    for nomor, snr in enumerate(data, start=1):
        status = kualitas_sinyal(snr)
        print(f"{nomor:02d}. SNR = {snr:>5.1f} dB -> {status}")

    jumlah = hitung_kategori(data)
    rata, maksimum, minimum = statistik(data)

    print("\n" + "=" * 58)
    print("RINGKASAN")
    print("=" * 58)
    print(f"Total data       : {len(data)}")
    print(f"RENDAH           : {jumlah['RENDAH']}")
    print(f"BAIK             : {jumlah['BAIK']}")
    print(f"SANGAT BAIK      : {jumlah['SANGAT BAIK']}")
    print(f"Rata-rata SNR    : {rata:.2f} dB")
    print(f"Maksimum SNR     : {maksimum:.2f} dB")
    print(f"Minimum SNR      : {minimum:.2f} dB")


if __name__ == "__main__":
    tampilkan_hasil(data_snr)
