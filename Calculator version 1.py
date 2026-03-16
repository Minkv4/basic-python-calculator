#Minks Claculator Project.
#Base menu code.
while True:
    print("\n=== MAIN MENU ===")
    print("1. Start Calculator")
    print("2. Exit Program")
    choice = input("Choose an option: ")
    if choice == "1":
#Calculator menu code.
        while True:
            print("\n=== CALCULATOR ===")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Back to Main Menu")
            calc_choice = input("Choose an option: ")
            if calc_choice == "5":
                break
            if calc_choice in ["1", "2", "3", "4"]:
#Calculation code.
                try:
                    num1 = float(input("Enter first number: "))
                except ValueError:
                    print("Please enter a valid number")
                    num1 = float(input("Enter first number: "))
                try:
                    num2 = float(input("Enter Second number: "))
                except ValueError:
                    print("Please enter a valid number")
                    num2 = float(input("Enter Second number: "))
                if calc_choice == "1":
                    result = num1 + num2
                elif calc_choice == "2":
                    result = num1 - num2
                elif calc_choice == "3":
                    result = num1 * num2
                elif calc_choice == "4":
                    if num2 == 0:
                        print("Cannot divide by zero")
                        continue
                    result = num1 / num2
                print("Result:", result)
            else:
                print("Invalid option")
#Main menu code.
    elif choice == "2":
        print("Program closed.")
        break
    else:
        print("Invalid choice")