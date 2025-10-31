def generate_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(key[i].lower()) - ord('a'))
            base = ord('A') if text[i].isupper() else ord('a')
            cipher_text.append(chr((ord(text[i]) - base + shift) % 26 + base))
        else:
            cipher_text.append(text[i])
    return "".join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = (ord(key[i].lower()) - ord('a'))
            base = ord('A') if cipher_text[i].isupper() else ord('a')
            orig_text.append(chr((ord(cipher_text[i]) - base - shift) % 26 + base))
        else:
            orig_text.append(cipher_text[i])
    return "".join(orig_text)

def main():
    print("=== Vigenere Cipher ===")
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci (keyword): ")
    key_full = generate_key(text, key)

    encrypted = vigenere_encrypt(text, key_full)
    decrypted = vigenere_decrypt(encrypted, key_full)

    print(f"\nHasil Enkripsi: {encrypted}")
    print(f"Hasil Dekripsi: {decrypted}")

if __name__ == "__main__":
    main()
