import hashlib
import getpass

def encrypt_password(password):
    
    return hashlib.md5(password.encode()).hexdigest()

def read_passwd_file(file_path):
    users = {}
    with open(file_path, 'r') as file:
        for line in file:
            username, real_name, encrypted_password = line.strip().split(':')
            users[username] = (real_name, encrypted_password)
    return users

def write_passwd_file(file_path, users):
    with open(file_path, 'w') as file:
        for username, (real_name, encrypted_password) in users.items():
            file.write(f"{username}:{real_name}:{encrypted_password}\n")

def user_exists(username, users):
    return username in users

def validate_password(username, password, users):
    if username in users:
        _, encrypted_password = users[username]
        return encrypt_password(password) == encrypted_password
    return False

def add_user():
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
    users = read_passwd_file(file_path)

    username = input("Enter username: ")

    if user_exists(username, users):
        del users[username]
        write_passwd_file(file_path, users)
        print("User Deleted")
    else:
        print("User not found")

def change_password():
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
