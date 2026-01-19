# Aplikasi game secret number

secret_number = 818

gues_number = int(input("masukkan tebak angka:"))


while gues_number != secret_number:
    print("tebakan salah, coba lagi!")
    print("anda terjebak") #modify
    gues_number = int(input("masukkan tebak angka"))

print ("selamat!!! tebakan anda benar!")
print("kode ini saya buat di codespace")