import random
import string

def generator():
    length = int(input("Enter password length: "))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"

    all_chars = lower + upper + digits + special

    # Ensure at least one of each
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill remaining length
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle password
    random.shuffle(password)

    password = ''.join(password)

    # Strength check
    strength = "Weak"
    if length >= 8:
        strength = "Medium"
    if length >= 12:
        strength = "Strong"

    print("\nGenerated Password:", password)
    print("Strength:", strength)

generator()