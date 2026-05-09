# Jordan Rinne
# jrinne@uci.edu
# ID: 16935997

import ui

def main():
    
    start = input("Enter a command: ")

    if start == "admin":
        ui.admin_mode()
    else:
        ui.main_ui(start)

    return None

if __name__ == "__main__":
    main()
    print("Goodbye!")
