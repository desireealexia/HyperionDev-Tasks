# simple calculator application that asks user to enter two numbers and the operation

print("Enter an equation. Equations must include two numbers and an operator (+, -, *, /) seperated by spaces.")
print("For example, 55 + 24 OR 765 * 89.")
# user inputs their choice of numbers and operator
while True:
    try:
        num1, operator, num2 = input("Enter your equation here: ").split()
        num1 = float(num1)
        num2 = float(num2)
        break
    except:
        print("Invalid input.")
        continue

operator = operator.lower()
while True:
    if operator == "+":
        result = num1 + num2
        print(f"{num1} {operator} {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} {operator} {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} {operator} {num2} = {result}")
    elif operator == "/":
            while True:
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                else:
                    result = num1 / num2
                    print(f"{num1} {operator} {num2} = {result}")
                    break
    else:
        print("Invalid input.")
    break

# append on text file
with open('equations.txt', 'a') as file:
    file.write(f"{num1} {operator} {num2} = {result} \n")

# check if user wants another calculation
while True:
    try:
        print("Do you want to do another calculation?")
        next_calculation = input("Please enter your choice here (yes/no): ")
        if next_calculation.lower() == 'yes':
            while True:
                try:
                    num1, operator, num2 = input("Enter another equation here: ").split()
                    num1 = float(num1)
                    num2 = float(num2)
                    break
                except:
                    print("Invalid input.")
                    continue
                
            operator = operator.lower()
            while True:
                if operator == "+":
                    result = num1 + num2
                    print(f"{num1} {operator} {num2} = {result}")
                elif operator == "-":
                    result = num1 - num2
                    print(f"{num1} {operator} {num2} = {result}")
                elif operator == "*":
                    result = num1 * num2
                    print(f"{num1} {operator} {num2} = {result}")
                elif operator == "/":
                    try:
                        result = num1 / num2
                        print(f"{num1} {operator} {num2} = {result}")
                        break
                    except ZeroDivisionError:
                        print("Cannot divide by zero!")
                        break
                else:
                    print("Invalid input.")
                break     

            # append on text file
            with open('equations.txt', 'a') as file:
                file.write(f"{num1} {operator} {num2} = {result} \n")

        # break the while loop if answer is no 
        elif next_calculation == 'no':
            print("Thank you for using our calculator!")
            break

    except ValueError:
        print("Please type in yes or no!")
    
#user is given a choice to enter an equation or read equations from a file.#
while True:
    print("Select one of the options below:")
    print("1. Enter an equation")
    print("2. Read equations from a file")
    print("3. Close")
    option_choice = input("Please enter your choice here (1, 2 or 3): ")

    # user inputs choice 1 - to enter an equation
    if option_choice == '1':
        try:
            while True:
                try:
                    num1, operator, num2 = input("Enter your equation here: ").split()
                    num1 = float(num1)
                    num2 = float(num2)
                    break
                except:
                    print("Invalid input.")
                    continue

            operator = operator.lower()
            while True:
                if operator == "+":
                    result = num1 + num2
                    print(f"{num1} {operator} {num2} = {result}")
                elif operator == "-":
                    result = num1 - num2
                    print(f"{num1} {operator} {num2} = {result}")
                elif operator == "*":
                    result = num1 * num2
                    print(f"{num1} {operator} {num2} = {result}")
                elif operator == "/":
                    result = num1 / num2
                    print(f"{num1} {operator} {num2} = {result}")
                else:
                    print("Invalid input.")
                break

            # append on text file
            with open('equations.txt', 'a') as file:
                file.write(f"{num1} {operator} {num2} = {result} \n")

        except ZeroDivisionError:
            print("Cannot divide by zero!")
            break

    # user inputs choice 2 - read from a file
    elif option_choice == '2':
        file_name = input("Please enter the file name here: ")
        while True:
            try:
                with open(file_name, 'r') as file:
                    print(file.read())
                    break
            except FileNotFoundError:
                print("Error, file now found. Please enter the file name again")
                file_name = input("Please enter the file name here: ")


    # user inputs choice 3 - to close application
    elif option_choice == '3':
        print("Thank you!")
        break

    else:
        print("Invalid input.")
