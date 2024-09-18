def main():
    while True:
        choice = input("Enter '1' to encrypt\nEnter '2' to decrypt\nEnter 'exit' to terminate\nEnter your choice: ")
        
        if choice == "1":
            print("-------------------------------------")
            message = input(" Enter a message: ")
            key = input(" Enter a key: ")
            encrypted_message = encrypt(message, key)
            print(" Encrypted text =", encrypted_message)
            print("-------------------------------------")
        
        elif choice == "2":
            print("-------------------------------------")
            message = input(" Enter a message: ")
            key = input(" Enter a key: ")
            decrypted_message = decrypt(message, key)
            print(" Decrypted text =", decrypted_message)
            print("-------------------------------------")
        
        elif choice == "exit":
            print("-------------------------------------")
            print(" Thank you")
            print("-------------------------------------")
            break
        
        else:
            print("-------------------------------------")
            print(" Invaid Choice... try again")
            print("-------------------------------------")


def adjust_key(key, message):
    while len(key) < len(message):
        key += key
    key =key[:len(message)]
    return key


def encrypt(message, key):
    new_key = adjust_key(key, message)
    encrypted_message = ""
    
    for char_message, char_key in zip(message, new_key):
        if char_message.islower():
            key_ascii = ord(char_key.lower())
            message_ascii = ord(char_message)
            new_pos = ((message_ascii - 97) + (key_ascii - 97)) % 26 + 97
            encrypted_message += chr(new_pos)

        elif char_message.isupper():
            key_ascii = ord(char_key.upper())
            message_ascii = ord(char_message)
            new_pos = ((message_ascii - 65) + (key_ascii - 65)) % 26 + 65
            encrypted_message += chr(new_pos)

        else:
            encrypted_message += char_message
    
    return encrypted_message


def decrypt(message, key):
    new_key = adjust_key(key, message)
    decrypted_message = ""
    
    for char_message, char_key in zip(message, new_key):
        if char_message.islower():
            key_ascii = ord(char_key.lower())
            message_ascii = ord(char_message)
            new_pos = ((message_ascii - 97) - (key_ascii - 97)) % 26 + 97
            decrypted_message += chr(new_pos)

        elif char_message.isupper():
            key_ascii = ord(char_key.upper())
            message_ascii = ord(char_message)
            new_pos = ((message_ascii - 65) - (key_ascii - 65)) % 26 + 65
            decrypted_message += chr(new_pos)

        else:
            decrypted_message += char_message
    
    return decrypted_message


if __name__ == "__main__":
    main()
