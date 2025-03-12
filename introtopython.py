

num1 = float(input("Enter 1st number: ")) #converts user input into a float number.
num2 = float(input("Enter 2nd number: ")) #converts user input into a float number.
operator = input("Enter operator (+ - * /): ") #allows user to select operator.



if operator == "+":             # checks operator selected by user.
    result = num1 + num2
    print(round(result, 2))     # prints result to 2 decimal places.

elif operator == "-":           # checks operator selected by user.
    result = num1 - num2
    print(round(result, 2))     # prints result to 2 decimal places.
elif operator == "*":           # checks operator selected by user.
    result = num1 * num2
    print(round(result, 2))     # prints result to 2 decimal places.

elif operator == "/":           # checks operator selected by user.
    result = num1 / num2
    if num2 == 0:               # checks if user hasn't entered 0 
        print("Error: Division by zero!") # prints if user has entered 0.
    else:                      
        print(round(result, 2)) # prints result to 2 decimal places.
else:
    print(f"{operator} is not valid. Please enter a valid operator.") # prints when user has used an invalid operator.
    quit()
    