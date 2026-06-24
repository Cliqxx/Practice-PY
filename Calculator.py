
print("WELCOME TO THE CALCULATOR")

user_input1 = 0
user_input2 = 0
total = 0
is_Running = True
while is_Running:
    cal = input("Enter the number of operation:\n 1. Add\n 2. Subtract\n 3. Multiplication\n 4. Divide\n (q to quit): ")

    if cal.lower() == 'q':
        print("Thank you for using this calculator")
        is_Running = False
    elif cal == '1':
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))
        total = user_input1 + user_input2
        print("The sum is: ", total)
    elif cal == '2':
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))
        total = user_input1 - user_input2
        print("The difference is: ", total)
    elif cal =='3':
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))
        total = user_input1 * user_input2
        print("The product is: ", total)
    elif cal == '4':
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))
        if user_input2 == 0:
            print("Complex Infinity")
        else:
            total = user_input1 / user_input2
            print("The quotient is: ", total)
    else:
        print("Invalid input")
