def remove_duplicates(key):
    """Menghapus karakter yang berulang dalam kunci."""
    seen = set()
    unique_key = []
    
    for char in key:
        if char.lower() not in seen:
            seen.add(char.lower())
            unique_key.append(char)
    
    return ''.join(unique_key)

def vigenere_encrypt(plaintext, key):
    # Menghapus karakter yang berulang dari kunci
    key = remove_duplicates(key)
    
    encrypted_text = ""
    key_length = len(key)
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():  # Mengecek apakah karakter adalah huruf
            # Menghitung shift dari kunci
            shift = ord(key[key_index % key_length].lower()) - ord('a')
            # Menghitung pergeseran untuk karakter plaintext
            if char.islower():
                encrypted_char = (ord(char) - ord('a') + shift) % 26 + ord('a')
            else:
                encrypted_char = (ord(char) - ord('A') + shift) % 26 + ord('A')
            
            encrypted_text += chr(encrypted_char)
            key_index += 1  # Hanya menambah index kunci jika huruf valid
        else:
            encrypted_text += char  # Jika bukan huruf, tetap sama

    return encrypted_text

# Input manual dari pengguna
plaintext = input("Masukkan plaintext: ")
key = input("Masukkan kunci: ")

if plaintext and key:  # Memastikan input tidak kosong
    encrypted = vigenere_encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
else:
    print("Plaintext dan kunci tidak boleh kosong.")
