# Exception Handling - Creating a simple app calculator
# Phoebe Rhone L. Gangoso | BSCPE 1-4

import pyfiglet
print("")
title_text = " Simple App Calculator "
title_line = title_text.center(150, "*")
print(title_line)
print("")
def calculator_app():
    try:
        # Ask user to choose and input math operation
        input_operation = input("\033[0;35m Choose one math operation (Addition, Subtraction, Multiplication, Division): ")
        # Ask user to input two numbers
        first_number = float(input("\033[0;33m Enter your first number: "))
        second_number = float(input(" Enter your second number: "))
        # Do the calculation
        # if addition
        if input_operation == "Addition":
            result_number = first_number + second_number
        # if subtraction
        elif input_operation == "Subtraction":
            result_number = first_number - second_number
        # if multiplication
        elif input_operation == "Multiplication":
            result_number = first_number * second_number
        # if division
        elif input_operation == "Division":
            result_number = first_number / second_number
        else:
            raise ValueError("Invalid math operation")
        # display result
        print("\033[0;34m Answer:", result_number)
        # ask user if they want to try again or not
        retry_input = input("\033[0;32m Do you want to try again? (Yes/No): ")
        # if yes repeat
        if retry_input == "Yes":
            calculator_app()
        else:
            print("\033[0;35m Thank you for using this calculator!\N{slightly smiling face}")

    # catch exceptions
    except ValueError as e:
        print(f"\033[0;34m Error: {e}. Please try again.")
        calculator_app()
    except ZeroDivisionError:
        print("\033[0;34m Error: Cannot divide by zero. Please try again.")
        calculator_app()

calculator_app()
