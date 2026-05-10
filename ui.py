# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jordan Rinne
# jrinne@uci.edu
# 16935997


import Profile as p
from pathlib import Path
from shlex import split as parse


def run_error(error_type="UNKNOWN EXCEPTION", friendly=True):
    if not friendly:
        print("ERROR")
        return None
    
    messages = {
        "INVALID COMMAND": "Invalid command. Use 'C' to create a file, 'D' to delete a file, 'R' to read a file, 'O' to open a file, 'E' to edit a profile, and 'P' to print profile information.",
        "INVALID COMMAND (E)": "Invalid edit command. Use '-usr' to edit username, '-pwd' to edit password, '-bio' to edit bio, '-addpost' to add a post, and '-delpost' to delete a post.",
        "INVALID COMMAND (P)": "Invalid print command. Use '-all' to print all profile information, '-usr' to print username, '-pwd' to print password, '-bio' to print bio, '-posts' to print all posts, and '-post <index>' to print a specific post.",
        "INPUT NUMBER ERROR": "Input number error. Ensure that you are providing the correct number of arguments for the command.",
        "PATH ERROR": "Path error. Ensure that the file path you provided is valid and that you have the necessary permissions to access it.",
        "FILE ERROR": "File error. Ensure that the file you are trying to access exists and is a valid .dsu file.",
        "PROFILE ERROR": "Profile error. Ensure that the profile you are trying to access is valid and that you have the necessary permissions to access it.",
    }

    if error_type in messages:
        print(f"{messages[error_type]} Check your input and try again.")
    else:
        print("UNKNOWN EXCEPTION: An unknown error occurred.")


def create_file(user_input, friendly=True):
    if len(user_input) != 3 or user_input[1] != "-n":
        run_error()
        return None
    directory = user_input[0]
    filename = user_input[2]
    file_path = Path(directory).expanduser() / f"{filename}.dsu"
    if file_path.exists():
        return file_path, True

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch(exist_ok=True)
    except Exception:
        run_error()
        return None
    
    if user_input[0][-1] != "/":
        user_input[0] += "/"
    print(f"{user_input[0]}{user_input[2]}.dsu CREATED")
    return file_path, False


def delete_file(user_input, friendly=True):
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


def read_file(user_input, friendly=True):
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


def open_file(user_input, friendly=True):
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
        try:
            data = f.read()
            if data == "":
                run_error()
                return None
            else:
                profile = p.Profile()
                profile.load_profile(str(FILE))
                print(f"{name} OPENED")
                return profile, FILE
        except Exception:
            run_error()
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


def check_profile(profile, friendly=True):

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
    

def edit_profile(user_input, profile, path, friendly=True):
    
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
            post = p.Post(entry=user_input[1])
            profile.add_post(post)
            profile.save_profile(path)
            user_input = user_input[2:]

        elif user_input[0] == "-delpost":
            try:
                index = int(user_input[1])
                if not profile.del_post(index):
                    run_error()
                    return None
                profile.save_profile(path)
                user_input = user_input[2:]
            except ValueError:
                run_error()
                return None
        
        else:
            run_error()
            return None
    return None


def print_profile(user_input, profile, friendly=True):

    if profile is None:
        run_error()
        return None

    if len(user_input) < 1:
        run_error()
        return None
    
    while len(user_input) > 0:
    
        if user_input[0] == "-all":
            if not check_profile(profile):
                return None
            posts = profile.get_posts()
            for i, post in enumerate(posts):
                print(f"Post {i}: {post.entry} (timestamp: {post.timestamp})")
            user_input = user_input[1:]

        elif user_input[0] == "-usr":
            print(f"Username: {profile.username}")
            user_input = user_input[1:]

        elif user_input[0] == "-pwd":
            print(f"Password: {profile.password}")
            user_input = user_input[1:]

        elif user_input[0] == "-bio":
            print(f"Bio: {profile.bio}")
            user_input = user_input[1:]

        elif user_input[0] == "-posts":
            posts = profile.get_posts()
            for i, post in enumerate(posts):
                print(f"Post {i}: {post.entry} (timestamp: {post.timestamp})")
            user_input = user_input[1:]

        elif user_input[0] == "-post" and len(user_input) >= 2 and user_input[1].isdigit():
            index = int(user_input[1])
            posts = profile.get_posts()
            post = posts[index] if 0 <= index < len(posts) else None
            if post is None:
                run_error()
                return None
            print(f"Post {index}: {post.entry} (timestamp: {post.timestamp})")
            user_input = user_input[2:]

        else:
            run_error()
            return None


def admin_mode():
    ans = " "
    profile = None
    file_path = None

    while True:
        try:
            ans = parse(input('Enter a command (Q to quit): '))
        except Exception:
            run_error(friendly=False)
            continue

        if not ans:
            run_error(friendly=False)
            continue
        if ans[0].lower() == "q":
            break

        if ans[0] == "C":
            result = create_file(ans[1:])
            if result is None:
                continue
            file_path, exists = result
            if not exists:
                profile = create_profile()
                profile.save_profile(str(file_path))
            if exists:
                try:
                    profile = p.Profile()
                    profile.load_profile(str(file_path))
                except Exception:
                    run_error(friendly=False)
                
        elif ans[0] == "D":
            delete_file(ans[1:])

        elif ans[0] == "R":
            read_file(ans[1:])

        elif ans[0] == "O":
            result = open_file(ans[1:])
            if result is not None:
                profile, file_path = result

        elif ans[0] == "E":
            try:
                edit_profile(ans[1:], profile, file_path)
            except Exception as e:
                run_error(friendly=False)

        elif ans[0] == "P":
            print_profile(ans[1:], profile)
            
        else:
            run_error(friendly=False)

    return None


def main_ui(start):
    pass
