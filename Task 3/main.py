#!/bin/python3

import string
import random
from rich.console import Console

console = Console()

def passwordGenerator(length = 10):
    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def prPurple(skk): 
    print("\033[1m\033[92m {}\033[00m".format(skk))
    
def main():
    while True:
        try:
            length = int(input("Enter the desired password length (default is 10): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        print()

        password = passwordGenerator(length)
        print(f"Generated password:", end=" ")
        prPurple(password)
        print()

        choice = input("Do you want to generate another password? (Y/N): ").lower()
        if choice!= 'y':
            break
        print()


if __name__ == '__main__':
    main()