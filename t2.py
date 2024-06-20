while True:
    number1 = float(input("Enter the number1: "))
    number2 = float(input("Enter the number2: "))
    choice = input("Enter operation \n1. addition \n2. subtraction\n3. multiplication\n4. division\n5. mod\n6. exit\n")

    if choice == '1':
        print("Addition of n1 and n2 = " + str(number1 + number2))
    elif choice == '2':
        print("Subtraction of n1 and n2 = " + str(number1 - number2))
    elif choice == '3':
        print("Multiplication of n1 and n2 = " + str(number1 * number2))
    elif choice == '4':
        if number2 != 0:
            print("Division of n1 and n2 = " + str(number1 / number2))
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == '5':
        if number2 != 0:
            print("Mod of n1 and n2 = " + str(number1 % number2))
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == '6':
        print("Program terminated.")
        break
    else:
        print("Invalid operator")