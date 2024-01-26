import hashlib
import getpass

def encrypt_password(password):
    """
    Encrypts the given password using the MD5 hash function.

    Parameters:
    - password (str): The password to be encrypted.

    Returns:
    str: The hexadecimal representation of the MD5 hash of the password.
    """

    return hashlib.md5(password.encode()).hexdigest()

def read_passwd_file(file_path):
    """
    Reads a password file and returns a dictionary containing user information.

    Parameters:
    - file_path (str): The path to the password file.

    Returns:
    dict: A dictionary where keys are usernames and values are tuples containing real names and encrypted passwords.
    """
  
    users = {}
    with open(file_path, 'r') as file:
        for line in file:
            username, real_name, encrypted_password = line.strip().split(':')
            users[username] = (real_name, encrypted_password)
    return users

def write_passwd_file(file_path, users):
        """
    Writes user information to a password file.

    Parameters:
    - file_path (str): The path to the password file.
    - users (dict): A dictionary where keys are usernames and values are tuples containing real names and encrypted passwords.
    """

        with open(file_path, 'w') as file:
            for username, (real_name, encrypted_password) in users.items():
                file.write(f"{username}:{real_name}:{encrypted_password}\n")

def user_exists(username, users):
    """
    Checks if a user with the given username exists in the provided user dictionary.

    Parameters:
    - username (str): The username to check.
    - users (dict): A dictionary where keys are usernames and values are tuples containing real names and encrypted passwords.

    Returns:
    bool: True if the user exists, False otherwise.
    """

    return username in users

def validate_password(username, password, users):
    """
    Validates a password for a given username against the stored encrypted password.

    Parameters:
    - username (str): The username to validate.
    - password (str): The password to validate.
    - users (dict): A dictionary where keys are usernames and values are tuples containing real names and encrypted passwords.

    Returns:
    bool: True if the password is valid, False otherwise.
    """

    if username in users:
        _, encrypted_password = users[username]
        return encrypt_password(password) == encrypted_password
    return False

def add_user():
    """
    Adds a new user to the password file, prompting for username, real name, and password.
    Prints appropriate messages based on success or failure.
    """
    users = read_passwd_file(file_path)

    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")

    if user_exists(username, users):
        print("Cannot add. Most likely username already exists.")
    else:
        encrypted_password = encrypt_password(password)
        users[username] = (real_name, encrypted_password)
        write_passwd_file(file_path, users)
        print("User Created.")

def delete_user():
    """
    Deletes a user from the password file, prompting for the username.
    Prints appropriate messages based on success or failure.
    """
    users = read_passwd_file(file_path)

    username = input("Enter username: ")

    if user_exists(username, users):
        del users[username]
        write_passwd_file(file_path, users)
        print("User Deleted")
    else:
        print("User not found")

def change_password():
    """
    Changes the password for an existing user, prompting for the current password and the new password.
    Prints appropriate messages based on success or failure.
    """
    users = read_passwd_file(file_path)

    username = input("User: ")

    if user_exists(username, users):
        current_password = getpass.getpass("Current Password: ")
        if validate_password(username, current_password, users):
            new_password = getpass.getpass("New Password: ")
            confirm_password = getpass.getpass("Confirm: ")

            if new_password == confirm_password:
                users[username] = (users[username][0], encrypt_password(new_password))
                write_passwd_file(file_path, users)
                print("Password changed")
            else:
                print("Passwords do not match")
        else:
            print("Invalid current password")
    else:
        print("User not found")

def login():
    """
    Authenticates a user by prompting for the username and password.
    Prints "Access granted" if authentication is successful, "Access denied" otherwise.
    """
    users = read_passwd_file(file_path)

    username = input("User: ")
    password = getpass.getpass("Password: ")

    if validate_password(username, password, users):
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    file_path = r"passwd.txt"
    while True:
        print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            change_password()
        elif choice == "4":
            login()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
