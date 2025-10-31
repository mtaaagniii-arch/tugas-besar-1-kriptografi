def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan nilai shift (misal 3): "))

    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"\nHasil Enkripsi: {encrypted}")
    print(f"Hasil Dekripsi: {decrypted}")

if __name__ == "__main__":
    main()
