# Exception Handling - Creating a simple app calculator
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# Ask user to choose and input math operation
input_operation = input("Choose one math operation (Addition, Subtraction, Multiplication, Division): ")
# Ask user to input two numbers
first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
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
# display result
print(result_number)
# ask user if they want to try again or not
# if yes repeat
