

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    filename = "sample.txt"   
    shift = 3                 

    try:
        with open(filename, "r") as f:
            content = f.read()

        encrypted = encrypt(content, shift)
        print("\n🔒 Encrypted Text:\n", encrypted)

        decrypted = decrypt(encrypted, shift)
        print("\n🔓 Decrypted Text:\n", decrypted)

    except FileNotFoundError:
        print("❌ File not found. Please check the filename.")
