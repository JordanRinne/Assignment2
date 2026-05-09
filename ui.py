# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Rinne
# jrinne@uci.edu
# 16935997


import Profile as p
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


def run_error():
    print("ERROR")
    return None


def create_profile():
    print("Let's Create Your Profile.")
    username = input("Username: ")
    password = input("Password: ")
    dsuserver = input("DsuServer: ")
    #bio = input("Bio: ")
    profile = p.Profile(dsuserver, username, password)
    print(f"Profile for user '{profile.username}' created!")
    return profile


def check_profile(profile):

    if profile is None:
        print("No Profile Found.")
        return False
    
    try:
        print("Profile Information:")
        print(f"Username: {profile.username}")
        print(f"Password: {profile.password}")
        print(f"DsuServer: {profile.dsuserver}")
        print(f"Bio: {profile.bio}")
        return True
    except Exception as e:
        print(f"Error occurred while checking profile: {e}")
        return False
    

def edit_profile(profile):
    if profile is None:
        print("No Profile Found.")
        return None
    
    print("Edit Your Profile Information:")
    username = input(f"Username ({profile.username}): ") or profile.username
    password = input(f"Password ({profile.password}): ") or profile.password
    dsuserver = input(f"DsuServer ({profile.dsuserver}): ") or profile.dsuserver
    bio = input(f"Bio ({profile.bio}): ") or profile.bio

    profile.username = username
    profile.password = password
    profile.dsuserver = dsuserver
    profile.bio = bio

    print("Profile updated successfully!")
    return profile


def main_ui(start_input):
    ans = " "
    profile = None
    while True:
        ans = input('Enter a command (Q to quit): ').split()
        if not ans:
            run_error()
            continue
        if ans[0].lower() == "q":
            break
        if ans[0] == "C":

            if check_profile(profile):
                file_path = create_file(ans[1:])
                profile.save_profile(str(file_path))
            else:
                profile = create_profile()
                file_path = create_file(ans[1:])
                profile.save_profile(str(file_path))
                
        elif ans[0] == "D":
            delete_file(ans[1:])
        elif ans[0] == "R":
            read_file(ans[1:])
        elif ans[0] == "O":
            open_file(ans[1:])
        else:
            run_error()
    check_profile(profile)
    return None
