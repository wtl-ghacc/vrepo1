def check_users(current_users, new_users):
    pass
    current_users = ['chris', 'haritha', 'sally', 'darnell', 'superman']
    new_users = ['george', 'ringo', 'superman', 'hannibal']

    current_users_lower = [user.lower() for user in current_users]

    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print("The username, " + new_user + ", is taken.")
        else:
            print("The username, " + new_user + ", is available.")

if __name__ == "__main__":
    current_us = ['chris', 'haritha', 'sally', 'darnelll', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)
