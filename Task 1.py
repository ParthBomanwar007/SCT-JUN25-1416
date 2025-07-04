def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result
while True:
    print("\nCaesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Choose option (1-3): ")

    if choice == '3':
        print("Exiting...")
        break
    if choice not in ['1', '2']:
        print("Invalid choice!")
        continue

    message = input("Enter message: ")
    try:
        shift = int(input("Enter shift value (1-25): "))
        if not 1 <= shift <= 25:
            print("Shift must be 1-25!")
            continue
        result = caesar_cipher(message, shift, encrypt=(choice == '1'))
        print(f"{'Encrypted' if choice == '1' else 'Decrypted'}: {result}")
    except ValueError:
        print("Invalid shift value!")
