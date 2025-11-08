# --- Simple Console Calculator Program ---

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero gracefully."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    """Main function to run the calculator application."""
    print("--- Simple Python Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Loop to ensure a valid choice is made
    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                # Get the numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            # Perform the calculation based on the user's choice
            result = None
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            # Print the result
            print(f"\nResult: {num1} {['+', '-', '*', '/'][int(choice) - 1]} {num2} = {result}\n")

            # Ask if the user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Exiting calculator. Goodbye!")
                break
        else:
            print("Invalid Input. Please select a valid operation (1, 2, 3, or 4).")

# Execute the main calculator function
if __name__ == "__main__":
    calculator()