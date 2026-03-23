import random
import string

def get_complexity_choice():
    print("\nSelect password complexity:")
    print("  1. Low       (letters only)")
    print("  2. Medium    (letters + digits)")
    print("  3. High      (letters + digits + symbols)")
    print("  4. Custom    (you choose character types)")

    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return choice
        print("  Invalid choice. Please enter a number between 1 and 4.")

def get_custom_charset():
    print("\nCustomize your character set:")
    charset = ""

    use_upper = input("  Include uppercase letters? (yes/no): ").strip().lower()
    if use_upper in ("yes", "y"):
        charset += string.ascii_uppercase

    use_lower = input("  Include lowercase letters? (yes/no): ").strip().lower()
    if use_lower in ("yes", "y"):
        charset += string.ascii_lowercase

    use_digits = input("  Include digits? (yes/no): ").strip().lower()
    if use_digits in ("yes", "y"):
        charset += string.digits

    use_symbols = input("  Include symbols? (yes/no): ").strip().lower()
    if use_symbols in ("yes", "y"):
        charset += string.punctuation

    if not charset:
        print("  No character types selected. Defaulting to all character types.")
        charset = string.ascii_letters + string.digits + string.punctuation

    return charset

def build_charset(choice):
    if choice == "1":
        return string.ascii_letters, "Low (letters only)"
    elif choice == "2":
        return string.ascii_letters + string.digits, "Medium (letters + digits)"
    elif choice == "3":
        return string.ascii_letters + string.digits + string.punctuation, "High (letters + digits + symbols)"
    elif choice == "4":
        charset = get_custom_charset()
        return charset, "Custom"

def generate_password(length, charset):
    # Ensure randomness using secrets-style shuffle
    password = [random.choice(charset) for _ in range(length)]
    random.shuffle(password)
    return "".join(password)

def password_strength(length, charset_size):
    import math
    entropy = length * math.log2(charset_size)
    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Fair"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"

def password_generator():
    print("=" * 45)
    print("        🔐 Python Password Generator")
    print("=" * 45)

    # Get desired password length
    while True:
        try:
            length = int(input("\nEnter desired password length (4–128): "))
            if 4 <= length <= 128:
                break
            else:
                print("  Please enter a length between 4 and 128.")
        except ValueError:
            print("  Invalid input. Please enter a whole number.")

    # Get complexity
    choice = get_complexity_choice()
    charset, complexity_label = build_charset(choice)

    # Ask how many passwords to generate
    while True:
        try:
            count = int(input("\nHow many passwords to generate? (1–10): "))
            if 1 <= count <= 10:
                break
            else:
                print("  Please enter a number between 1 and 10.")
        except ValueError:
            print("  Invalid input. Please enter a whole number.")

    # Generate and display passwords
    print("\n" + "-" * 45)
    print(f"  Complexity : {complexity_label}")
    print(f"  Length     : {length} characters")
    print(f"  Strength   : {password_strength(length, len(charset))}")
    print("-" * 45)

    passwords = [generate_password(length, charset) for _ in range(count)]

    if count == 1:
        print(f"\n  Generated Password:\n\n    {passwords[0]}\n")
    else:
        print(f"\n  Generated Passwords:\n")
        for i, pwd in enumerate(passwords, 1):
            print(f"    {i}. {pwd}")
        print()

    print("-" * 45)
    print("  Tip: Store your password in a secure password manager.")
    print("-" * 45)

# Run in a loop
if __name__ == "__main__":
    while True:
        password_generator()
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nStay safe and secure. Goodbye! 🔒")
            break
        print()
