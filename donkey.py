import banner
import menu


def start():
    banner.print_banner()

    print("\nWould you like to select a character? yes or no")

    answer = input(" > ").lower()

    if answer == "yes":
        menu.main_menu()

    elif answer == "no":
        exit()

    else:
        print("INVALID Selection!")

        start()

start()