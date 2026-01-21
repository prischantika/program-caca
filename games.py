import random

# Database makanan Indonesia dengan hint daerah
makanan_database = [
    {
        "nama": "rendang",
        "daerah": "Sumatera Barat",
        "hint": "Makanan berkuah merah yang terkenal dari daerah penghasil kopi ☕"
    },
    {
        "nama": "soto ayam",
        "daerah": "Jawa",
        "hint": "Sup kuning dengan ayam yang sangat populer di seluruh Indonesia 🍗"
    },
    {
        "nama": "gado-gado",
        "daerah": "Jawa",
        "hint": "Sayuran yang dicampur dengan saus kacang yang nikmat 🥜"
    },
    {
        "nama": "satay",
        "daerah": "Indonesia",
        "hint": "Daging tusuk yang dipanggang dan disajikan dengan saus kacang 🍢"
    },
    {
        "nama": "bakso",
        "daerah": "Jawa Timur",
        "hint": "Bola daging dalam kuah kaldu yang hangat 🍖"
    },
    {
        "nama": "martabak",
        "daerah": "Indonesia",
        "hint": "Terang bulan yang gurih atau manis, populer di malam hari 🌙"
    },
    {
        "nama": "nasi kuning",
        "daerah": "Indonesia",
        "hint": "Nasi yang dimasak dengan santan dan dibumbui kunyit 💛"
    },
    {
        "nama": "lumpia",
        "daerah": "Semarang",
        "hint": "Makanan goreng yang berisi daging dan sayuran, renyah di mulut 😋"
    },
    {
        "nama": "tahu goreng",
        "daerah": "Indonesia",
        "hint": "Makanan dari kedelai yang digoreng sampai kuning keemasan 🟡"
    },
    {
        "nama": "perkedel",
        "daerah": "Indonesia",
        "hint": "Makanan dari umbi-umbian yang dikukus lalu digoreng 🥔"
    },
    {
        "nama": "sop buntut",
        "daerah": "Jawa",
        "hint": "Sup panas dengan buntut sapi yang empuk 🔥"
    },
    {
        "nama": "nasi goreng",
        "daerah": "Indonesia",
        "hint": "Nasi yang digoreng dengan telur dan berbagai lauk pauk 🍚"
    }
]

def tampilkan_banner():
    """Menampilkan banner game yang menarik"""
    print("=" * 50)
    print("🎮 SELAMAT DATANG DI GAME TEBAK MAKANAN INDONESIA! 🎮")
    print("=" * 50)
    print("✨ Tebak nama makanan populer dari berbagai daerah! ✨")
    print("📍 Kamu punya 3 kesempatan untuk setiap makanan!")
    print("=" * 50)
    print()

def main_game():
    """Fungsi utama game"""
    tampilkan_banner()
    
    # Pilih makanan random dari database
    makanan = random.choice(makanan_database)
    nama_makanan = makanan["nama"]
    daerah = makanan["daerah"]
    hint = makanan["hint"]
    
    skor = 0
    kesempatan = 3
    
    print(f"🍽️  PUTARAN BARU! 🍽️")
    print(f"📍 Hint Daerah Asal: {daerah}")
    print(f"💡 Petunjuk: {hint}")
    print(f"❤️  Kesempatan: {kesempatan}x")
    print()
    
    while kesempatan > 0:
        tebakan = input(f"🤔 Coba tebak nama makanannya (kesempatan sisa: {kesempatan}): ").lower().strip()
        
        # Cek apakah tebakan benar
        if tebakan == nama_makanan:
            print()
            print("🎉🎉🎉 BOOM, KAMU BERHASIL! 🎉🎉🎉")
            print(f"✅ Jawaban yang benar adalah: {nama_makanan.upper()} dari {daerah}!")
            print("Mantap jiwa! Kamu hebat! 💪✨")
            skor += 1
            print()
            return skor
        
        # Cek apakah tebakan hampir benar (edit distance)
        elif tebakan in nama_makanan or nama_makanan.split()[0] == tebakan:
            print()
            print("AYOO, SEDIKIT LAGI! 🔥🔥")
            print("Jawabanmu sudah mendekati... semangat terus! 💪")
            print()
            kesempatan -= 1
        
        # Tebakan salah
        else:
            print()
            print("o ow... kamu salah, silahkan coba lagi! 😅")
            print(f"Sabar yaa, masih ada {kesempatan - 1} kesempatan lagi!")
            print()
            kesempatan -= 1
    
    # Jika semua kesempatan habis
    print()
    print("💥 BOOM, KAMU GAGAL MENEBAK! 💥")
    print(f"😢 Jawaban yang benar adalah: {nama_makanan.upper()} dari {daerah}!")
    print(f"💡 Petunjuknya: {hint}")
    print("Jangan sedih, coba lagi yaa! Semoga beruntung di putaran berikutnya! 🍀")
    print()
    return skor

def permainan_lengkap():
    """Permainan dengan multiple rounds"""
    lanjut = True
    skor_total = 0
    putaran = 0
    
    while lanjut:
        putaran += 1
        print(f"{'='*50}")
        print(f"PUTARAN KE-{putaran}")
        print(f"{'='*50}")
        
        skor = main_game()
        skor_total += skor
        
        print(f"📊 SKOR SAAT INI: {skor_total}/{putaran}")
        print()
        
        while True:
            pilihan = input("🎮 Mau bermain lagi? (ya/tidak): ").lower().strip()
            if pilihan in ['ya', 'y']:
                lanjut = True
                break
            elif pilihan in ['tidak', 'n', 'tidak']:
                lanjut = False
                break
            else:
                print("❌ Pilihan tidak valid! Ketik 'ya' atau 'tidak'")
        
        if not lanjut:
            print()
            print("=" * 50)
            print("🏆 TERIMA KASIH TELAH BERMAIN! 🏆")
            print(f"📊 SKOR AKHIR: {skor_total}/{putaran}")
            if skor_total == putaran:
                print("🌟 SEMPURNA! Kamu master tebak makanan! 🌟")
            elif skor_total >= putaran * 0.7:
                print("👍 Bagus! Pengetahuanmu tentang makanan Indonesia sudah bagus!")
            else:
                print("💪 Jangan menyerah! Coba lagi lain kali dan pelajari makanan Indonesia!")
            print("Sampai jumpa lagi! 👋✨")
            print("=" * 50)

# Jalankan program
if __name__ == "__main__":
    permainan_lengkap()
