# Password Generator (CLI)

This Python script generates strong, random passwords using a combination of uppercase letters, lowercase letters, digits, and special characters. It provides an interactive command-line interface where users can specify the desired password length and generate multiple passwords as needed.

---

## Features

- Generates passwords with a mix of uppercase letters, lowercase letters, digits, and special characters.
- Ensures passwords are at least 8 characters long.
- Interactive user interface for specifying password length and generating multiple passwords.
- Uses colored output to highlight generated passwords.

---

## Requirements

- Python 3.x

## Code Explanation

1. **Imports:**
   - `string`: Provides constants for different character sets.
   - `random`: Used to generate random choices from character sets.

2. **Function `passwordGenerator(length=10)`:**
   - Defines character sets for uppercase letters, lowercase letters, digits, and special characters.
   - Combines all character sets into one.
   - Generates a random password of the specified length by selecting random characters from the combined set.
   - Returns the generated password.

3. **Function `prPurple(skk)`:**
   - Prints the input string `skk` in purple color.

4. **Main Program Execution:**
   - Continuously prompts the user to enter the desired password length.
   - Validates that the length is at least 8 characters and is a valid integer.
   - Generates and displays the password in purple.
   - Asks the user if they want to generate another password or exit the program.

---

TASK 3 for **Encryptix** Internship
