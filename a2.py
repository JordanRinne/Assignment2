# Jordan Rinne
# jrinne@uci.edu
# ID: 16935997

import ui

def main():
    start = input()
    
    if start == "admin":
        ui.admin_mode()
    else:
        ui.ui(start)

    return None

if __name__ == "__main__":
    main()
    print("Goodbye!")
