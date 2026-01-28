#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from collections import defaultdict

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed = []
        
    def add_task(self, task, emoji, reminder, category):
        """Menambahkan task ke dalam to-do list"""
        self.tasks.append({
            'task': task,
            'emoji': emoji,
            'reminder': reminder,
            'category': category,
            'completed': False
        })
    
    def display_tasks(self):
        """Menampilkan semua task yang belum selesai"""
        print("=" * 70)
        print(f"📋 TO-DO LIST HARIAN - {datetime.now().strftime('%d %B %Y')}")
        print("=" * 70)
        
        categories = defaultdict(list)
        
        for idx, task in enumerate(self.tasks, 1):
            if not task['completed']:
                categories[task['category']].append((idx, task))
        
        if not categories:
            print("✅ Selamat! Semua tugas sudah selesai!")
            return
        
        for category in ['🌅 Pagi', '🏫 Sekolah', '🏠 Rumah', '💪 Kesehatan', '📚 Belajar', '🎮 Hiburan', '🌙 Malam']:
            if category in categories:
                print(f"\n{category}")
                print("-" * 70)
                for idx, task in categories[category]:
                    print(f"  {idx}. {task['emoji']} {task['task']}")
                    print(f"     ⏰ {task['reminder']}")
                    print()
    
    def mark_completed(self, task_num):
        """Menandai task sebagai selesai"""
        if 0 < task_num <= len(self.tasks):
            self.tasks[task_num - 1]['completed'] = True
            print(f"✅ Tugas '{self.tasks[task_num - 1]['task']}' sudah selesai!")
            return True
        return False
    
    def show_all(self):
        """Menampilkan semua task termasuk yang sudah selesai"""
        print("=" * 70)
        print("📋 SEMUA TO-DO LIST")
        print("=" * 70)
        
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task['completed'] else "⏳"
            print(f"{status} {idx}. {task['emoji']} {task['task']}")
            print(f"   ⏰ {task['reminder']}")
            print()

# Inisialisasi To-Do List
my_tasks = ToDoList()

# ===== AKTIVITAS PAGI =====
my_tasks.add_task(
    "Membereskan tempat tidur",
    "🛏️",
    "06:00 - Bangun pagi dan langsung membereskan tempat tidur!",
    "🌅 Pagi"
)

my_tasks.add_task(
    "Mandi dan merapikan diri",
    "🚿",
    "06:15 - Mandi pagi untuk memulai hari dengan segar",
    "🌅 Pagi"
)

my_tasks.add_task(
    "Sarapan pagi",
    "🥣",
    "06:45 - Jangan lupa sarapan untuk energi sepanjang hari",
    "🌅 Pagi"
)

my_tasks.add_task(
    "Bersiap ke sekolah",
    "👕",
    "07:00 - Pakai pakaian dan siapkan perlengkapan sekolah",
    "🌅 Pagi"
)

# ===== AKTIVITAS SEKOLAH =====
my_tasks.add_task(
    "Berangkat ke sekolah tepat waktu",
    "🚌",
    "07:30 - Jangan terlambat! Berangkat ke sekolah",
    "🏫 Sekolah"
)

my_tasks.add_task(
    "Mengikuti pembelajaran di kelas",
    "📖",
    "07:45 - Fokus dan dengarkan penjelasan guru dengan baik",
    "🏫 Sekolah"
)

my_tasks.add_task(
    "Mengerjakan tugas sekolah/PR",
    "✏️",
    "16:00 - Segera kerjakan PR sebelum bermain",
    "🏫 Sekolah"
)

my_tasks.add_task(
    "Mempersiapkan perlengkapan untuk hari besok",
    "🎒",
    "20:00 - Cek buku dan alat tulis untuk besok",
    "🏫 Sekolah"
)

# ===== AKTIVITAS RUMAH =====
my_tasks.add_task(
    "Merapikan kamar",
    "🧹",
    "17:00 - Buang sampah dan rapikan barang-barang di kamar",
    "🏠 Rumah"
)

my_tasks.add_task(
    "Membantu orang tua di rumah",
    "👨‍👩‍👧",
    "17:30 - Tanya apa yang bisa kamu bantu untuk keluarga",
    "🏠 Rumah"
)

my_tasks.add_task(
    "Mencuci piring/peralatan makan",
    "🍽️",
    "19:00 - Bantu bersihkan peralatan makan setelah makan",
    "🏠 Rumah"
)

my_tasks.add_task(
    "Merapikan ruang keluarga",
    "🪑",
    "18:00 - Kembalikan barang ke tempatnya dengan rapi",
    "🏠 Rumah"
)

# ===== AKTIVITAS KESEHATAN =====
my_tasks.add_task(
    "Olahraga/bermain di luar",
    "🏃",
    "15:00 - Minimal 30 menit aktivitas fisik untuk kesehatan",
    "💪 Kesehatan"
)

my_tasks.add_task(
    "Minum air putih yang cukup",
    "💧",
    "Setiap jam - Minum air 8 gelas per hari untuk tubuh yang sehat",
    "💪 Kesehatan"
)

my_tasks.add_task(
    "Cuci tangan sebelum makan",
    "🧼",
    "Sebelum setiap makan - Kebiasaan baik untuk mencegah penyakit",
    "💪 Kesehatan"
)

my_tasks.add_task(
    "Sikat gigi dua kali sehari",
    "🦷",
    "07:00 & 21:00 - Pagi dan malam untuk gigi yang sehat",
    "💪 Kesehatan"
)

# ===== AKTIVITAS BELAJAR =====
my_tasks.add_task(
    "Membaca buku/materi pelajaran",
    "📚",
    "18:00 - 19:00 - Pelajari materi yang sudah diajarkan hari ini",
    "📚 Belajar"
)

my_tasks.add_task(
    "Mengerjakan soal latihan",
    "🔢",
    "19:00 - 20:00 - Kerjakan soal-soal untuk memperkuat pemahaman",
    "📚 Belajar"
)

my_tasks.add_task(
    "Menulis ringkasan pelajaran",
    "📝",
    "20:00 - 20:30 - Catat hal-hal penting dalam buku catatan",
    "📚 Belajar"
)

# ===== AKTIVITAS HIBURAN =====
my_tasks.add_task(
    "Bermain game/hobi favorit",
    "🎮",
    "15:30 - 16:30 - Relaksasi setelah sekolah (maksimal 1 jam)",
    "🎮 Hiburan"
)

my_tasks.add_task(
    "Nonton film/video edukatif",
    "📺",
    "20:30 - 21:00 - Hiburan yang menghibur sekaligus mendidik",
    "🎮 Hiburan"
)

my_tasks.add_task(
    "Bermain dengan teman/keluarga",
    "👫",
    "Kapan saja - Habiskan waktu bersama orang-orang terkasih",
    "🎮 Hiburan"
)

# ===== AKTIVITAS MALAM =====
my_tasks.add_task(
    "Makan malam bersama keluarga",
    "🍽️",
    "19:00 - Nikmati waktu makan malam bersama keluarga",
    "🌙 Malam"
)

my_tasks.add_task(
    "Bersiap tidur (mandi malam)",
    "🚿",
    "20:30 - Mandi dan persiapkan diri untuk tidur nyenyak",
    "🌙 Malam"
)

my_tasks.add_task(
    "Tidur tepat waktu",
    "😴",
    "21:30 - Tidur 8-9 jam untuk istirahat optimal",
    "🌙 Malam"
)

my_tasks.add_task(
    "Refleksi harian (doa/dzikir)",
    "🙏",
    "21:00 - Berdoa/dzikir sebelum tidur",
    "🌙 Malam"
)

# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    print("\n🌟 SELAMAT DATANG DI APLIKASI TO-DO LIST HARIAN 🌟\n")
    
    # Menampilkan semua task
    my_tasks.display_tasks()
    
    print("\n" + "=" * 70)
    print("💡 TIPS PENTING:")
    print("=" * 70)
    print("""
✨ Jangan lupa:
   • Selalu bangun pagi dan berangkat tepat waktu ke sekolah
   • Kerjakan PR segera setelah tiba di rumah
   • Bantu orang tua dalam pekerjaan rumah tangga
   • Olahraga dan istirahat yang cukup untuk kesehatan
   • Disiplin diri membuat hidup lebih teratur dan sukses
   • Jangan lupa berdoa di pagi dan malam hari
   
🎯 CARA MENGGUNAKAN:
   1. Cek task apa yang belum dikerjakan
   2. Kerjakan sesuai prioritas dan reminder
   3. Tandai sebagai selesai setelah dikerjakan
   4. Terus konsisten setiap hari!
    """)
    print("=" * 70)
    print("🚀 Tetap semangat! Kamu pasti bisa! 💪")
    print("=" * 70 + "\n")
