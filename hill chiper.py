import numpy as np

def mod_inverse_matrix(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det % modulus, -1, modulus)
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_mod_inv % modulus

def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(n % 26 + ord('A')) for n in numbers)

def hill_encrypt(text, key_matrix):
    text_nums = text_to_numbers(text)
    while len(text_nums) % key_matrix.shape[0] != 0:
        text_nums.append(ord('X') - ord('A'))
    text_matrix = np.array(text_nums).reshape(-1, key_matrix.shape[0])
    encrypted = np.dot(text_matrix, key_matrix) % 26
    return numbers_to_text(encrypted.flatten())

def hill_decrypt(cipher, key_matrix):
    inv_key = mod_inverse_matrix(key_matrix, 26)
    cipher_nums = text_to_numbers(cipher)
    cipher_matrix = np.array(cipher_nums).reshape(-1, key_matrix.shape[0])
    decrypted = np.dot(cipher_matrix, inv_key) % 26
    return numbers_to_text(decrypted.flatten())

def main():
    print("=== Hill Cipher ===")
    text = input("Masukkan teks: ")

    print("\nMasukkan matriks kunci (2x2):")
    a11 = int(input("a11: ")); a12 = int(input("a12: "))
    a21 = int(input("a21: ")); a22 = int(input("a22: "))

    key_matrix = np.array([[a11, a12], [a21, a22]])

    encrypted = hill_encrypt(text, key_matrix)
    decrypted = hill_decrypt(encrypted, key_matrix)

    print(f"\nHasil Enkripsi: {encrypted}")
    print(f"Hasil Dekripsi: {decrypted}")

if __name__ == "__main__":
    main()
