# Data buah dalam satu list menyangkut nama, harga, total penjualan dan target penjualan
buah_list = [
    {
        "nama": "Apel",
        "harga": 5000,  
        "jual": [21, 19, 20, 18, 20, 25, 18],
        "target": 1000000 
    },
    {
        "nama": "Jeruk",
        "harga": 40000,
        "jual": [20, 22, 19, 24, 21, 19, 19],
        "target": 900000
    },
    {
        "nama": "Pisang",
        "harga": 3500,
        "jual": [21, 19, 17, 16, 15, 17, 16],
        "target": 750000
    },
    {
        "nama": "Mangga",
        "harga": 4500,
        "jual": [21, 19, 17, 19, 11, 16, 21],
        "target": 950000
    }
]

# list hari dalam 1 minggu penuh
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

print("\n=== Laporan Penjualan Buah per Hari ===\n")

# perulangan untuk menghitung jumlah pendapatan harian per buah
for buah in buah_list:
    nama = buah['nama']
    harga = buah['harga']
    jual = buah['jual']
    target = buah['target']
    # Ambil data buah: nama, harga, daftar penjualan, dan target
    
    pendapatan = [j * harga for j in jual]
    # Hitung pendapatan harian: jumlah terjual * harga
    total = sum(pendapatan)
    # Jumlahkan total pendapatan selama seminggu
    maks = max(pendapatan)
    # Cari pendapatan harian tertinggi
    skala = 50 / maks  # Panjang bar disesuaikan dgn nilai tertinggi pendapatan harian buah itu
    # Skala untuk visualisasi bar (50 karakter dibagi nilai maksimum)

    print(f"\n--- {nama.upper()} ---")
    # Cetak nama buah dalam huruf besar
    for i in range(7):
        bar = '█' * int(pendapatan[i] * skala)
        # Buat bar visual dengan panjang proporsional ke pendapatan
        print(f"{hari[i]:<8} | Rp {pendapatan[i]:>3} | {bar}")
        # Cetak hari, pendapatan, dan bar visual

    # Evaluasi terhadap target
    if total >= target:
        print(f"\nTarget tercapai untuk buah {nama} (Total: Rp {total})")
    elif total >= 0.5 * target:
        print(f"\nHampir mencapai target untuk buah {nama} (Total: Rp {total})")
    else:
        print(f"\nButuh usaha lebih keras untuk buah {nama} (Total: Rp {total})")
    # Cek apakah total pendapatan memenuhi target (100%, ≥50%, atau <50%)

# Cari buah apel dari list
for buah in buah_list:
    if buah['nama'].lower() == 'apel':
        # Cari buah "Apel" (case-insensitive)
        harga = buah['harga']
        jual = buah['jual']
        target = buah['target']
        # Ambil data apel: harga, penjualan, dan target
        
        pendapatan = [j * harga for j in jual]  # pendapatan harian
        # Hitung pendapatan harian apel
        akumulasi = 0
        tercapai = False
        batas = 0.75 * target
        # Inisialisasi akumulasi, status pencapaian, dan batas 75% target

        for i in range(7):
            akumulasi += pendapatan[i]
            # Tambahkan pendapatan harian ke akumulasi
            if akumulasi >= batas:
                print(f"\nPendapatan apel telah mencapai ≥ 75% dari target (Rp {batas}) pada hari {hari[i]} (Hari ke-{i+1})")
                tercapai = True
                break
            # Cek kapan akumulasi mencapai 75% target, cetak hari dan hentikan loop

        if not tercapai:
            print("\nPendapatan apel belum mencapai 75% dari target setelah seminggu.")
        # Jika tidak tercapai, cetak pesan
        break
    # Hentikan loop setelah menemukan apel

print("\n=== Laju Perubahan Pendapatan Hari ke-6 ke 7 ===\n")
# Cetak judul laporan laju perubahan

for buah in buah_list:
    nama = buah['nama']
    harga = buah['harga']
    jual = buah['jual']
    pendapatan = [j * harga for j in jual]
    # Ambil data buah dan hitung pendapatan harian

    delta = pendapatan[6] - pendapatan[5]  # Minggu - Sabtu
    # Hitung selisih pendapatan hari ke-7 dan ke-6
    status = "meningkat" if delta > 0 else "menurun" if delta < 0 else "tetap"
    # Tentukan status berdasarkan selisih (positif, negatif, atau nol)

    print(f"Laju perubahan {nama} dari hari 6 ke 7 : Rp{delta:+} per hari ({status}).")
    # Cetak laju perubahan dan status