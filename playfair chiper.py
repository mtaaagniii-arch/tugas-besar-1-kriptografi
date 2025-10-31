def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    if char == 'J':
        char = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def process_text(text):
    text = text.upper().replace("J", "I")
    processed = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            processed += a + 'X'
            i += 1
        else:
            processed += a + b
            i += 2
    if len(processed) % 2 != 0:
        processed += 'X'
    return processed

def playfair_encrypt(text, key_matrix):
    text = process_text(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(key_matrix, a)
        row2, col2 = find_position(key_matrix, b)
        if row1 == row2:
            result += key_matrix[row1][(col1 + 1) % 5]
            result += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += key_matrix[(row1 + 1) % 5][col1]
            result += key_matrix[(row2 + 1) % 5][col2]
        else:
            result += key_matrix[row1][col2]
            result += key_matrix[row2][col1]
    return result

def playfair_decrypt(text, key_matrix):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(key_matrix, a)
        row2, col2 = find_position(key_matrix, b)
        if row1 == row2:
            result += key_matrix[row1][(col1 - 1) % 5]
            result += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += key_matrix[(row1 - 1) % 5][col1]
            result += key_matrix[(row2 - 1) % 5][col2]
        else:
            result += key_matrix[row1][col2]
            result += key_matrix[row2][col1]
    return result

def main():
    print("=== Playfair Cipher ===")
    key = input("Masukkan kunci: ")
    text = input("Masukkan teks: ")

    matrix = generate_key_matrix(key)
    encrypted = playfair_encrypt(text, matrix)
    decrypted = playfair_decrypt(encrypted, matrix)

    print(f"\nHasil Enkripsi: {encrypted}")
    print(f"Hasil Dekripsi: {decrypted}")

if __name__ == "__main__":
    main()
