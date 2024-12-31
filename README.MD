README Content for GitHub Repository
    markdown
    Copy code
# Secret Message Encryption and Decryption

This repository contains a simple Python script for encrypting and decrypting secret messages. It provides an easy-to-use interface for encoding and decoding messages with a custom encryption scheme. The script also includes a user-friendly prompt to choose between encryption and decryption.

---

## 🚀 Features

- **Custom Encryption Scheme**: Encodes words with unique prefixes, suffixes, and rearranged characters.
- **Decryption Functionality**: Restores the original message from its encrypted form.
- **Interactive User Input**: Guides users to choose encryption or decryption via a menu.
- **Reversal for Short Words**: Words with three or fewer characters are reversed as part of the encryption process.

---

## 🛠️ Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Aashu-destined/Secret_Encrypted_msg.git
   cd Secret_Encrypted_msg

2. **Run the Script**:
    python secret_message.py

3. Follow the Prompts:

    -Enter your message.
    -Choose whether to encrypt or decrypt.
    -View the result on the terminal.

📋 Example
Encryption
Input:
hello world python

Output:
tyellohnxl lrow tynthonpynxl

Decryption
Input:
tyellohnxl lrow tynthonpynxl

Output:
hello world python

🔍 How It Works
Encryption
    Splits the message into words.
    For words with more than 3 characters:
    Adds the prefix tyi and suffix nxl.
    Rearranges the first and remaining characters.
    For words with 3 or fewer characters:
    Reverses the characters.
Decryption
    Splits the message into words.
    For words with tyi prefix and nxl suffix:
    Removes them and rearranges the characters to their original form.
    For words with 3 or fewer characters:
    Reverses the characters.


📜 Code Overview
Functions
    encrypt(msg): Encrypts a given message.
    decrypt(msg): Decrypts an encrypted message.
    salect(msg): Prompts the user to choose between encryption and decryption.
    run(msg): Executes the selected operation and displays the result.
Entry Point
The script starts execution from the if __name__ == "__main__": block, where it accepts user input and processes the message.


🔧 Customization
Modify the prefixes and suffixes in the encrypt and decrypt functions for a personalized encryption scheme.
Adjust the logic for short words to suit your requirements.


🖥️ Dependencies
Python 3.x
No additional libraries are required.

🤝 Contributing
Feel free to fork this repository, make improvements, and submit a pull request! Suggestions and feedback are always welcome.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
For questions or collaboration:

GitHub: Aashu-destined



































A python program to translate a message into secret code language.

Encryption Rules:
    If the word contains atleast 3 characters, remove the first letter and append it at the end
        now append three random characters at the starting and the end
    else
        simply revers the string

Dycryption Rules:
    You may guesss
