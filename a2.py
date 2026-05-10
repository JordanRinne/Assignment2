# Jordan Rinne
# jrinne@uci.edu
# ID: 16935997

import ui


def main():

    print("Welcome to the DSU Profile Manager!")
    start = input("To get started, would you like to create a new profile "
    "or load an existing one? (new/load): ").strip().lower()

    if start == "admin":
        ui.admin_mode()
    else:
        ui.main_ui(start)

    return None


if __name__ == "__main__":
    main()
    print("Okay, Hope you enjoyed using the program! Goodbye, and have a great day!")
    print()
