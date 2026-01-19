# Aplikasi game secret number

secret_number = 818

gues_number = int(input("masukkan tebak angka: 🤔"))


while gues_number != secret_number:
    if gues_number < secret_number:
        print("salah, tebakan anda terlalu rendah ⬆️")
    else:
        print("kurang tepat, tebakan anda terlalu tinggi ⬇️")
    gues_number = int(input("masukkan tebak angka: 🤔"))

print ("selamat!!! tebakan anda benar! 🎉")
print("kode ini saya buat di codespace 💻")