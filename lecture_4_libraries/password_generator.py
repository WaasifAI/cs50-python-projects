# Password Generator using random and string libraries
import random
import string

def generate_password(length):
    if length < 8:
        return "Password should be at least 8 characters for security."

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print(" Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        result = generate_password(length)
        print(f" Your secure password: {result}")
    except ValueError:
        print(" Please enter a valid number.")

if __name__ == "__main__":
    main()
