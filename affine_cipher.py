import math
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def affine_encrypt(plaintext, a, b):
    ciphertext = ""
    m = 26  
    for char in plaintext:
        if char.isalpha():
            char_value = ord(char.upper()) - ord('A')
            encrypted_value = (a * char_value + b) % m
            encrypted_char = chr(encrypted_value + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext
def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    m = 26  
    a_inverse = mod_inverse(a, m)
    if a_inverse is None:
        return "Error: 'a' is not invertible."
    for char in ciphertext:
        if char.isalpha():
            char_value = ord(char.upper()) - ord('A')
            decrypted_value = (a_inverse * (char_value - b)) % m
            decrypted_char = chr(decrypted_value + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext
plaintext = "HELLO, WORLD!"
a = 5
b = 8
encrypted_text = affine_encrypt(plaintext, a, b)
print("Encrypted text:", encrypted_text)
decrypted_text = affine_decrypt(encrypted_text, a, b)
print("Decrypted text:", decrypted_text)
