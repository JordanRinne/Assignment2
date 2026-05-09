# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Rinne
# jrinne@uci.edu
# 16935997


import Profile as p
from pathlib import Path
from shlex import split as parse


def run_error():
    print("ERROR")
    return None


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
    return file_path


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


def create_profile():

    dsuserver = input("DsuServer: ")
    username = input("Username: ")
    password = input("Password: ")
    bio = input("Bio: ")

    profile = p.Profile(dsuserver, username, password)
    profile.bio = bio
    print(f"Profile for user '{profile.username}' created")
    return profile


def check_profile(profile):

    if profile is None:
        run_error()
        return False
    
    try:
        print(f"DsuServer: {profile.dsuserver}")
        print(f"Username: {profile.username}")
        print(f"Password: {profile.password}")
        print(f"Bio: {profile.bio}")
        return True
    except Exception as e:
        run_error()
        return False
    
"""
def in_quotes(str:str):

    if (str[0] == '"' or str[0] == "'") and (str[-1] == '"' or str[-1] == "'"):
        return True
    else:
        return False
"""

def edit_profile(user_input, profile, path):
    
    #commands = ["-usr", "-pwd", "-bio", "-addpost", "-delpost"]

    if len(user_input) < 2:
        run_error()
        return None
    
    while len(user_input) > 1:
        if user_input[0] == "-usr" and " " not in user_input[1]:
            profile.username = user_input[1]
            profile.save_profile(path)
            user_input = user_input[2:]
        elif user_input[0] == "-pwd" and " " not in user_input[1]:
            profile.password = user_input[1]
            profile.save_profile(path)
            user_input = user_input[2:]
        elif user_input[0] == "-bio":
            profile.bio = user_input[1]
            profile.save_profile(path)
            user_input = user_input[2:]
        elif user_input[0] == "-addpost":
            profile.add_post(user_input[1])
            profile.save_profile(path)
            user_input = user_input[2:]
        elif user_input[0] == "-delpost":
            try:
                index = int(user_input[1])
                profile.delete_post(index)
                profile.save_profile(path)
                user_input = user_input[2:]
            except ValueError:
                run_error()
                return None
        else:
            run_error()
            return None
                                  
    
    return None


def admin_mode():
    ans = " "
    profile = None
    while True:

        try:
            ans = parse(input('Enter a command (Q to quit): '))
        except Exception:
            run_error()
            continue

        if not ans:
            run_error()
            continue
        if ans[0].lower() == "q":
            break
        if ans[0] == "C":

            profile = create_profile()
            file_path = create_file(ans[1:])
            profile.save_profile(str(file_path))
                
        elif ans[0] == "D":
            delete_file(ans[1:])
        elif ans[0] == "R":
            read_file(ans[1:])
        elif ans[0] == "O":
            open_file(ans[1:])


        elif ans[0] == "E":

            try:
                edit_profile(ans[1:], profile, file_path)
            except Exception as e:
                print(f"Error occurred while editing profile: {e}")

        else:
            run_error()

    
    return None


def main_ui(start):
    pass
