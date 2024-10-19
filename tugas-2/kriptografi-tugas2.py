def caesar_cipher(plaintext, key):
    result = ""

    # Loop setiap karakter di plaintext
    for char in plaintext:
        # Enkripsi huruf besar
        if char.isupper():
            # Shift karakter sesuai key, dan bungkus dengan 26 huruf alfabet
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Enkripsi huruf kecil
        elif char.islower():
            # Shift karakter sesuai key, dan bungkus dengan 26 huruf alfabet
            result += chr((ord(char) + key - 97) % 26 + 97)
        # Karakter non-huruf tidak berubah
        else:
            result += char

    return result

# Input teks yang ingin di Enskripsi
plaintext = input("Masukkan plaintext: ")
key = int(input("Masukkan kunci (shift): "))

# Hasil dari enkripsi
ciphertext = caesar_cipher(plaintext, key)
print("Ciphertext:", ciphertext)
