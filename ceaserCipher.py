def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char

    return result

plaintext = input("Enter the value to encrypt : ")
shift_value = int(input("Enter the key value : "))
ciphertext = caesar_cipher(plaintext, shift_value)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
