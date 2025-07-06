# Robust Calculator using functions and exception handling

def calculator(num_1, num_2):
    try:
        choice = input('Enter choice (+, -, *, /, //, %): ')

        if choice == '+':
            print(f'Addition: {num_1 + num_2}')
        elif choice == '-':
            print(f'Subtraction: {num_1 - num_2}')
        elif choice == '*':
            print(f'Multiplication: {num_1 * num_2}')
        elif choice == '/':
            print(f'Division: {num_1 / num_2}')
        elif choice == '//':
            print(f'Floor Division: {num_1 // num_2}')
        elif choice == '%':
            print(f'Modulus: {num_1 % num_2}')
        else:
            print('INVALID CHOICE')

    except ZeroDivisionError:
        print("Cannot divide by zero.")


# Main function that gets user input and calls calculator
def main():
    print("Welcome to Waasif's Calculator")

    try:
        num_1 = float(input("Enter num_1: "))
        num_2 = float(input("Enter num_2: "))
        calculator(num_1, num_2)

    except ValueError:
        print("Enter a valid number, please.")


# Entry point
if __name__ == "__main__":
    main()
