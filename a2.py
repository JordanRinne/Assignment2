# Jordan Rinne
# jrinne@uci.edu
# ID: 16935997

import ui

def main():
    
    print("Welcome to the DSU Profile Manager!")
    start = input("Enter a command to get started, or 'help' for a list of commands: ")

    if start == "admin":
        ui.admin_mode()
    else:
        ui.main_ui(start)

    return None

if __name__ == "__main__":
    main()
    print("Goodbye!")
