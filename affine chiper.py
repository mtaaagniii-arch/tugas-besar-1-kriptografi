def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - start) + b) % 26) + start)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Nilai 'a' tidak memiliki invers modulo 26!"
    for char in cipher:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * ((ord(char) - start) - b)) % 26) + start)
        else:
            result += char
    return result

def main():
    print("=== Affine Cipher ===")
    text = input("Masukkan teks: ")
    a = int(input("Masukkan nilai a (coprime dengan 26): "))
    b = int(input("Masukkan nilai b: "))

    encrypted = affine_encrypt(text, a, b)
    decrypted = affine_decrypt(encrypted, a, b)

    print(f"\nHasil Enkripsi: {encrypted}")
    print(f"Hasil Dekripsi: {decrypted}")

if __name__ == "__main__":
    main()
