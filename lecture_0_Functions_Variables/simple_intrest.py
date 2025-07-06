# Simple Interest Calculator using Python

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Main function
def main():
    # User input
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate: "))
    time = float(input("Enter the time in years: "))

    # Calculate interest
    interest = calculate_simple_interest(principal, rate, time)

    # Output result
    print(f"\nSimple Interest after {time} years is: ₹{interest:}")

# Run main
if __name__ == "__main__":
    main()
