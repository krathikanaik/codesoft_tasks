def calculator():
    while True:
        print("\n" + "=" * 25)
        print("    SIMPLE CALCULATOR    ")
        print("=" * 25)

        # Get the two numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("\nError: Invalid input! Please enter numerical values.")
            continue

        # Display operation options
        print("\nSelect Operation:")
        print("  + : Addition")
        print("  - : Subtraction")
        print("  * : Multiplication")
        print("  / : Division")

        operation = input("Enter operation (+, -, *, / or 1, 2, 3, 4): ").strip()

        # Perform calculation
        if operation in ("+", "1"):
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif operation in ("-", "2"):
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif operation in ("*", "3"):
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif operation in ("/", "4"):
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("\nError: Invalid operation choice!")

        # Ask if the user wants to repeat
        repeat = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if repeat not in ("yes", "y"):
            print("\nThank you for using the calculator! Goodbye.")
            break


if __name__ == "__main__":
    calculator()
