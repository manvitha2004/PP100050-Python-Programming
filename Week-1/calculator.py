import math

def cmd_calc():
    print(" Welcome to CalcHub - The Command-Line Calculator! \n")
    print("Available Operations:")
    print("1. Add (a)")
    print("2. Subtract (s)")
    print("3. Multiply (m)")
    print("4. Divide (d)")
    print("5. Power (p)")
    print("6. Square Root (r)")
    print("7. Exit (e)")

    while True:
        user_choic = input("\nSelect an operation (Enter key): ").lower()
        if user_choic in {"a", "s", "m", "d", "p"}:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            if user_choic == "a":
                result = add_them(num1, num2)
            elif user_choic == "s":
                result = subtract_them(num1, num2)
            elif user_choic == "m":
                result = multiply_them(num1, num2)
            elif user_choic == "d":
                result = divide_them(num1, num2)
            elif user_choic == "p":
                result = power_them(num1, num2)
            display_result(result)
        elif user_choic == "r":
            num = get_number("Enter the number to find its square root: ")
            result = sqrt_them(num)
            display_result(result)
        elif user_choic == "e":
            print("\nThank you for using CalcHub! Goodbye! ")
            break
        else:
            print("Invalid input. Please try again.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def add_them(a, b): return a + b
def subtract_them(a, b): return a - b
def multiply_them(a, b): return a * b

def divide_them(a, b):
    return a / b if b != 0 else "Error: Division by zero is undefined."

def power_them(a, b): return math.pow(a, b)
def sqrt_them(a): return math.sqrt(a) if a >= 0 else "Error: Negative input for square root."

def display_result(result):
    print(f"\n🔍 Result: {result}\n" if isinstance(result, (int, float)) else f"\n❌ {result}\n")

if __name__ == "__main__":
    cmd_calc()
