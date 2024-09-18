# Vigenère Cipher

A Python implementation of the Vigenère cipher that allows for both encryption and decryption of alphabetic text using a keyword.

## Features
- Encrypts messages using a provided key.
- Decrypts encrypted messages with the same key.
- Interactive console interface.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/Armaan2408/Vigenere-Cipher.git
    cd Vigenere-Cipher
    ```

2. Run the script:

    ```bash
    python Vigenere_cipher.py
    ```

3. Follow the on-screen prompts:

    - Enter `1` to encrypt a message.
    - Enter `2` to decrypt a message.
    - Enter `exit` to terminate the program.

## Example Usage

**Encryption:**

```bash
Enter '1' to encrypt
Enter '2' to decrypt
Enter 'exit' to terminate
Enter your choice: 1
-------------------------------------
Enter a message: HelloWorld
Enter a key: KEY
Encrypted text = RijvsUyvjn
-------------------------------------
Enter '1' to encrypt
Enter '2' to decrypt
Enter 'exit' to terminate
Enter your choice: 2
-------------------------------------
Enter a message: RijvsUyvjn
Enter a key: KEY
Decrypted text = HelloWorld
-------------------------------------
