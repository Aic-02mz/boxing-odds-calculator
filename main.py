print("Welcome to Boxing Odds Calculator!")
print("This program helps you convert between decimal and fractional odds.")
print("Please choose an option:")
print("1. Convert Decimal to Fractional Odds")
print("2. Convert Fractional to Decimal Odds")
print("3. Calculate Implied Probability ")
print("4. View Instructions/Help ")
print("5. Exit")


# defining a function to calculate HCF.
def calculate_hcf(x, y):
    while y:
        x, y = y, x % y
    return abs(x)


def help():
    print("Welcome to the Support Area!")
    print("This tool is designed to help you understand betting odds for boxing matches.")
    print("\nMenu Options Overview:")
    print("1. Convert Decimal Odds to Fractional Odds:")
    print("   - This option converts decimal odds to fractional format.")
    print("   - Simply input the decimal odds, and the program will display the equivalent fractional odds.")
    print("\n2. Convert Fractional Odds to Decimal Odds:")
    print("   - This option converts fractional odds to decimal format.")
    print(
        "- Enter the fractional odds in the format 'numerator/denominator', and the program will convert it to "
        "decimal odds.")
    print("\n3. Calculate Implied Probability:")
    print("   - This option calculates the implied probability based on the odds you provide.")
    print(
        "- Enter the odds (either decimal or fractional), and the program will display the implied probability as a "
        "percentage.")
    print("\n4. View Instructions/Help:")
    print(
        "- You are currently viewing this section, which provides guidance on how to use the program and understand "
        "its features.")
    print("\n5. Exit the Program:")
    print(
        "- Select this option to exit the program. You will be prompted to save any unsaved calculations before the "
        "program closes.")
    print("\nKey Concepts Explained:")
    print("   - Decimal Odds: odds but shown in decimal format .")
    print("   - Fractional Odds: odds but shown in fractional format .")
    print("   - Implied Probability: The likelihood of an outcome occurring, according to the odds.")
    print("\nCommon Errors and Troubleshooting:")
    print("   - Invalid Input: Follow the format guidelines provided by the program.")
    print("   - File Not Found: Ensure you enter the correct filename, including the file extension.")
    print("\nThank you for using the Boxing Odds Calculator. Good luck!")


def implied_pro():
    print("You Selected Implied Probability")
    print("Please choose the type of odds:")
    print("1. Decimal Odds")
    print("2. Fractional Odds")

    try:
        choose = int(input("Please choose the type of odds: "))
    except ValueError:
        print("Invalid input. Please enter a valid number (1 or 2).")
        return

    if choose == 1:
        try:
            decimal_odds = float(input("Please enter the decimal odds: "))
            if decimal_odds <= 0:
                print("Decimal odds must be greater than 0.")
                return
            probability = 1 / decimal_odds * 100
            print(f"The implied probability for decimal odds {decimal_odds} is {probability:.2f}%")
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")
    elif choose == 2:
        fractional_odds = input("Please enter the fractional odds (e.g., 5/2): ")
        try:
            numerator, denominator = map(float, fractional_odds.split('/'))
            if denominator == 0:
                print("Denominator cannot be zero.")
                return
            decimal_odds = numerator / denominator + 1
            probability = 1 / decimal_odds * 100
            print(f"The implied probability for fractional odds {fractional_odds} is {probability:.2f}%")
        except ValueError:
            print("Invalid fractional odds format. Please enter as 'numerator/denominator' (e.g., 5/2).")
    else:
        print("Invalid choice. Please select 1 or 2.")


def divide_hcf(numerator, denominator):
    hcf = calculate_hcf(numerator, denominator)
    a = numerator / hcf
    b = denominator / hcf
    fractional_odd = f"{int(a)}/{int(b)}"  # Formatted as a fraction
    return fractional_odd


def decimal():
    try:
        d = float(input("Enter Decimal odds: "))

        if d <= 0:
            print("Negative or zero Decimal odds are not supported.")
            return

        if d < 1:
            print("Negative odds less than 1 are not supported.")
            return

        minus = d - 1

        # Determine the precision needed
        precision = 10 ** 4  # This is done up to four decimal points
        numerator = round(minus * precision)
        denominator = precision

        # Simplify the fraction
        fractional_odd = divide_hcf(numerator, denominator)
        print(f"The fractional odds for {d} are {fractional_odd}.")

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")


def fractional():  # This is done and correct
    # Get fractional odds input as a string
    fraction = input("Enter fractional odds (in the form a/b): ")

    try:
        # Split the input string into numerator and denominator
        numerator, denominator = map(int, fraction.split('/'))

        # Check if the denominator is zero
        if denominator == 0:
            print(f"The denominator cannot be zero.")
            return
        if numerator == 0:
            print(f"The numerator cannot be zero.")
            return

        # Convert the fraction to decimal
        decimal_odds = numerator / denominator

        # Display the result
        print(f"The decimal odds for {fraction} is {decimal_odds}.")

    except (ValueError, ZeroDivisionError):
        # Handle invalid input (e.g., non-numeric values or incorrect format)
        print(f"Invalid input. Please enter the fraction in the form a/b.")


def main():
    while True:
        try:
            user_choice = int(input("Enter your choice one, type in a number between 1 and 5: ): "))
            if user_choice == 1:
                decimal()
            elif user_choice == 2:
                fractional()
            elif user_choice == 3:
                implied_pro()
            elif user_choice == 4:
                help()
            elif user_choice == 5:
                print(f"\nThank you for using Boxing Odds Calculator!")
                break
            else:
                print("Invalid input, Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        end = input("Would you like to exit? (type y to exit) or press any other key to continue: ").lower()
        if end == "y":
            break


if __name__ == "__main__":
    main()
