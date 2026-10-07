
import secrets
import string


def get_integer(prompt, minimum, maximum):
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            number = int(value)
            if minimum <= number <= maximum:
                return number

        print(f"Enter a number between {minimum} and {maximum}.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Please enter y or n.")


def generate_password(length, use_digits, use_symbols):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    characters = letters
    required = [secrets.choice(letters)]

    if use_digits:
        characters += digits
        required.append(secrets.choice(digits))

    if use_symbols:
        characters += symbols
        required.append(secrets.choice(symbols))

    if length < len(required):
        raise ValueError("Password length is too short.")

    password = required[:]

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    print("\n=== PYTHON PASSWORD GENERATOR ===")

    length = get_integer("Password length (1-128): ", 1, 128)
    count = get_integer("Number of passwords (1-20): ", 1, 20)

    use_digits = get_yes_no("Include numbers? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    minimum_length = 1 + int(use_digits) + int(use_symbols)

    if length < minimum_length:
        print(f"Choose a length of at least {minimum_length}.")
        return

    print("\nGenerated passwords:")

    for i in range(count):
        password = generate_password(
            length, use_digits, use_symbols
        )
        print(f"{i + 1}. {password}")


if __name__ == "__main__":
    main()
