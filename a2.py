# Jordan Rinne
# jrinne@uci.edu
# ID: 16935997

import Profile
import ui
from pathlib import Path


def create_file(user_input):
    if len(user_input) != 3 or user_input[1] != "-n":
        run_error()
        return None
    directory = user_input[0]
    filename = user_input[2]
    file_path = Path(directory).expanduser() / f"{filename}.dsu"
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch(exist_ok=True)
    if user_input[0][-1] != "/":
        user_input[0] += "/"
    print(f"{user_input[0]}{user_input[2]}.dsu CREATED")
    return None


def delete_file(user_input):
    if len(user_input) != 1:
        run_error()
        return None
    name = user_input[0]
    if name[-4:] != ".dsu":
        run_error()
        return None
    FILE = Path(name).expanduser()
    if not FILE.is_file():
        run_error()
        return None
    FILE.unlink()
    print(f"{name} DELETED")
    return None


def read_file(user_input):
    if len(user_input) != 1:
        run_error()
        return None
    name = user_input[0]
    if name[-4:] != ".dsu":
        run_error()
        return None
    FILE = Path(name).expanduser()
    if not FILE.is_file():
        run_error()
        return None
    with FILE.open() as f:
        if f.read() == "":
            print("EMPTY")
        else:
            f.seek(0)
            print("\n"+f.read()+"\n")
    return None


def open_file(user_input):
    if len(user_input) != 1:
        run_error()
        return None
    name = user_input[0]
    if name[-4:] != ".dsu":
        run_error()
        return None
    FILE = Path(name).expanduser()
    if not FILE.is_file():
        run_error()
        return None
    FILE.open()
    print(f"{name} OPENED")
    return None


def run_error():
    print("ERROR")
    return None


def create_profile(user_input):
    pass


def main():
    ans = " "
    while True:
        ans = input('Enter a command (Q to quit): ').split()
        if not ans:
            run_error()
            continue
        if ans[0].lower() == "q":
            break
        if ans[0] == "C":
            create_file(ans[1:])
        elif ans[0] == "D":
            delete_file(ans[1:])
        elif ans[0] == "R":
            read_file(ans[1:])
        elif ans[0] == "O":
            open_file(ans[1:])
        else:
            run_error()
    return None


if __name__ == "__main__":
    main()
    print("Goodbye!")
