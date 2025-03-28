# CLI Secure Password Generator

A simple yet powerful command-line password generator built in Python that creates secure, randomized passwords.

## Features

- Generates strong passwords with a mix of:
  - 8-10 random letters (both uppercase and lowercase)
  - 2-4 random symbols
  - 2-4 random numbers
- Randomizes character order for enhanced security
- Simple to use with no dependencies beyond Python's standard library

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/cli-password-generator.git
   cd cli-password-generator
   ```

2. No additional packages required - just Python!

## Usage

Run the password generator with:

```
python main.py
```

The program will output a secure password to the console.

## Example

```
$ python main.py
Your password is: aB7c$D9e*FgH2
```

## Security

Passwords are generated using Python's `random` module. Each password includes:

- A mix of uppercase and lowercase letters
- Numbers
- Special symbols
- Randomized order of characters

## License

This project is open source and available under the [MIT License](LICENSE).