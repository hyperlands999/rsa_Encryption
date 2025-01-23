from rsa import RSATool

def main():
    print("Welcome to the RSA Encryption/Decryption Tool!")
    rsa = RSATool()

    print("\nYour Public Key:")
    print(rsa.public_key.decode())

    print("\nYour Private Key (keep this secret!):")
    print(rsa.private_key.decode())

    action = input("\nDo you want to (e)ncrypt or (d)ecrypt? ").lower()
    if action == 'e':
        message = input("Enter the message to encrypt: ")
        public_key = input("Enter the recipient's public key: ")
        encrypted_message = rsa.encrypt(message, public_key)
        print(f"\nEncrypted Message: {encrypted_message}")
    elif action == 'd':
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = rsa.decrypt(encrypted_message)
        print(f"\nDecrypted Message: {decrypted_message}")
    else:
        print("Invalid action!")

if __name__ == "__main__":
    main()