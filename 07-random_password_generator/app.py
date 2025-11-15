import random
import string


def generate_password():
    length = int(input("Enter the desired password length: ").strip())

    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    special_chars = string.punctuation
    digits_chars = string.digits
    all_chars = lower_chars + upper_chars + special_chars + digits_chars

    required_chars = []

    required_chars.append(random.choice(lower_chars))
    required_chars.append(random.choice(upper_chars))
    required_chars.append(random.choice(special_chars))
    required_chars.append(random.choice(digits_chars))

    remaining_length = length - len(required_chars)

    password = required_chars

    for _ in range(remaining_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print(generate_password())
