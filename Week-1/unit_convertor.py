def unit_converter():

    print("\n Welcome to UnitX - The Unit Conversion Tool!\n")
    print("1. Length: Kilometers to Miles (k)")
    print("2. Weight: Kilograms to Pounds (w)")
    print("3. Temperature: Celsius to Fahrenheit (t)")
    print("4. Exit (e)")

    while True:
        choice = input("\nSelect a conversion (Enter key): ").lower()
        if choice == "k":
            km = pos_num("Enter distance in kilometers: ")
            result = km_to_miles(km)
            display_result(f"{km} kilometers is {result:.2f} miles.")
        elif choice == "w":
            kg = pos_num("Enter weight in kilograms: ")
            result = kg_to_pounds(kg)
            display_result(f"{kg} kilograms is {result:.2f} pounds.")
        elif choice == "t":
            celsius = get_number("Enter temperature in Celsius: ")
            result = celsius_to_fahrenheit(celsius)
            display_result(f"{celsius}°C is {result:.2f}°F.")
        elif choice == "e":
            print("\nThank you for using UnitX! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

def pos_num(prompt):
    while True:
        number = get_number(prompt)
        if number >= 0:
            return number
        print("Please enter a positive value.")


def km_to_miles(km): return km * 0.621371
def kg_to_pounds(kg): return kg * 2.20462
def celsius_to_fahrenheit(c): return (c * 9/5) + 32

def display_result(message):
    print(f"\n {message}\n")

if __name__ == "__main__":
    unit_converter()
