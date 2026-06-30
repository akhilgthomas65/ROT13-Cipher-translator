# ROT13 Cipher Translator

A simple Python program that encrypts and decrypts text using the **ROT13 cipher**. ROT13 is a letter substitution cipher that replaces each letter with the letter 13 positions later in the alphabet. Since the English alphabet contains 26 letters, applying the ROT13 cipher twice returns the original message.

## Features

* Encrypts plain text using the ROT13 cipher
* Decrypts ROT13-encoded text using the same program
* Preserves uppercase and lowercase letters
* Leaves numbers, spaces, and punctuation unchanged
* Simple command-line interface

## Requirements

* Python 3.x

## Installation

Clone this repository:

```bash
git clone https://github.com/akhilgthomas65/ROT13-Cipher-translator.git
```

Or clone using SSH:

```bash
git clone git@github.com:akhilgthomas65/ROT13-Cipher-translator.git
```

Navigate to the project directory:

```bash
cd ROT13-Cipher-translator
```

## Usage

Run the program:

```bash
python "ROT13 cipher converter.py"
```

### Example

```text
Enter a message:
Hello World!

Translated message:
Uryyb Jbeyq!
```

Running the program again with `Uryyb Jbeyq!` as the input will return:

```text
Hello World!
```

## How It Works

The program processes each character in the user's input. Alphabetic characters are shifted 13 positions through the alphabet while maintaining their case. Non-alphabetic characters, such as spaces, numbers, and punctuation, remain unchanged.

## Author

**Akhil G. Thomas**

GitHub: https://github.com/akhilgthomas65

## License

This project is open source and available under the MIT License.
