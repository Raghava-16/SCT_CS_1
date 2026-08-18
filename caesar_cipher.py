def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            # Keep spaces, numbers and special characters unchanged
            result += char

    return result


def main():
    print("===================================")
    print("       CAESAR CIPHER PROGRAM")
    print("===================================")

    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    print("\nChoose an option:")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        encrypted_text = caesar_cipher(message, shift)
        print("\nEncrypted Message:", encrypted_text)

    elif choice == "2":
        decrypted_text = caesar_cipher(message, -shift)
        print("\nDecrypted Message:", decrypted_text)

    else:
        print("\nInvalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()