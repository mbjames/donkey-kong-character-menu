def main_menu():
    print("\n Please select a character.")
    print(" 1. Donkey Kong")
    print(" 2. Diddy Kong")
    print(" 3. Dixie Kong")
    print(" 4. Cranky Kong")
    print(" 5. Funky Kong")

    answer = input("\n > ").lower()

    if answer == "1":
        print("\n You are Donkey Kong")

        main_menu()

    elif answer == "2":
        print("\n You are Diddy Kong")

        main_menu()

    elif answer == "3":
        print("\n You are Dixie Kong")

        main_menu()

    elif answer == "4":
        print("\n You are Cranky Kong")

        main_menu()

    elif answer == "5":
        print("\n You are Funky Kong")

        main_menu()

    else:
        print("INVALID SELECTION!")

        main_menu()
