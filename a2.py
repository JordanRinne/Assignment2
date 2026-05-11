# Jordan Rinne
# jrinne@uci.edu
# ID: 16935997


import ui


def main():
    print()
    print("Welcome to the DSU Profile Manager!")
    print()
    start = input(
        "To get started, would you like to create a new profile "
        "or open an existing one? (new/open): "
    ).strip().lower()

    if start == "admin":
        ui.admin_mode()
    else:
        ui.main_ui(start)

    return None


if __name__ == "__main__":
    main()
    print(
        "Okay, hope you enjoyed using the program!"
        " Goodbye, and have a great day!"
    )
    print()
