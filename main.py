import os
from miscellaneous import AccountManager
import constants


while True:  # Runs the Main Menu in loop
    os.system('cls')
    print(constants.logo)
    choice = input(constants.main_menu)
    print("")

    os.system('cls')  # Clear screen before processing user choice

    if choice == '1':
        current_user = AccountManager().register()
        input("Press Enter to continue...")
    elif choice == '2':
        AccountManager().load_users()
        current_user = AccountManager().login()
        if current_user is None:
            input("Press Enter to continue...")
        else:
            AccountManager().show_home(current_user)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")