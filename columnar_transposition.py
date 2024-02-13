def remove_whitespace(input_str):
    """Remove whitespaces from the input string."""
    return input_str.replace(" ", "")

def get_key():
    """Get a valid key length from user input."""
    while True:
        try:
            key_length = int(input("Enter the length of the key: "))
            if key_length > 0:
                return key_length
            else:
                print("Key length should be greater than 0. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_keys(key_length):
    """Get the keys from user input."""
    print("Enter the keys:")
    return [int(input()) for _ in range(key_length)]

def pad_string(input_str, key_length):
    """Pad the input string with '$' to make its length a multiple of key length."""
    remainder = len(input_str) % key_length
    if remainder != 0:
        padding = key_length - remainder
        input_str += "$" * padding
    return input_str

def encrypt(input_str, key):
    """Encrypt the input string using columnar transposition cipher."""
    encrypted_text = ""
    for i in range(len(key)):
        key_index = key.index(i + 1)
        encrypted_text += ''.join(input_str[j] for j in range(key_index, len(input_str), len(key)))
    return encrypted_text

def decrypt(cipher_text, key):
    """Decrypt the cipher text using columnar transposition cipher."""
    n_rows = len(cipher_text) // len(key)
    decrypted_lists = [[] for _ in range(n_rows)]
    key_order = [key.index(i + 1) for i in range(len(key))]
    
    chunks = [list(cipher_text[i:i + n_rows]) for i in range(0, len(cipher_text), n_rows)]
    
    for i, chunk in enumerate(chunks):
        for j, char in enumerate(chunk):
            decrypted_lists[j].insert(key_order[i], char)
    
    decrypted_text = ''.join([''.join(sublist) for sublist in decrypted_lists])
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    input_string = remove_whitespace(input("Enter the string data: "))
    key_length = get_key()
    key = get_keys(key_length)
    
    input_string = pad_string(input_string, key_length)
    
    cipher_text = encrypt(input_string, key)
    print("Encrypted Cipher text:", cipher_text)

    decrypt(cipher_text, key)
