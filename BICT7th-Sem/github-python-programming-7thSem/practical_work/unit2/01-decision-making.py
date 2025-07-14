# Menu-driven program using if, match, break, and continue statements

while True:
    print("\nMenu:")
    print("1. Check if a number is positive or negative")
    print("2. Display grade remarks (A, B, C, D, F)")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    # Using if statements
    if choice == '1':
        number = float(input("Enter a number: "))
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    # Using match statements
    elif choice == '2':
        grade = input("Enter your grade (A, B, C, D, F): ").upper()
        match grade:
            case "A":
                print("Excellent!")
            case "B":
                print("Good job!")
            case "C":
                print("You passed.")
            case "D":
                print("You barely passed.")
            case "F":
                print("Better luck next time.")
            case _:
                print("Invalid grade entered.")

    # Using break to exit
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    # Using continue for invalid input
    else:
        print("Invalid choice. Try again.")
        continue
