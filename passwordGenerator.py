import string
import random


def generate_password(password_length):
    use_lower = input("Do you use lowercase letters? (y/n) ").strip().lower() == "Y"
    use_upper = input("Do you use uppercase letters? (y/n) ").strip().lower() == "Y"
    use_digits = input("Do you use digits? (y/n) ").strip().lower() == "Y"
    use_symbols = input("Do you use symbols? (y/n) ").strip().lower() == "Y"

    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choice(characters) for _ in range(password_length))


def main():
    password_length = int(input("Enter password length: "))
    password = generate_password(password_length)
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
