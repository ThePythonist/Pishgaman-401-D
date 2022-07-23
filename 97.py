def signup(username, passwod):
    open("DB-USERS.txt","a+").write(username+"\n")
    open("DB-PASSWORDS.txt","a+").write(passwod+"\n")
    print("Account Created")


def signin():
    db_users = open("DB-USERS.txt","r")
    db_passwords = open("DB-PASSWORDS.txt","r")
    users = [ i[:-1] for i in db_users ]
    passwords = [ i[:-1] for i in db_passwords ]
    accounts = dict(zip(users,passwords))

    entry = input("Username : ")

    if entry in accounts :
        password = input("Password : ")
        if password == accounts[entry] :
            print("Login completed")
        else :
            print("Wrong password. Try again")
    else :
        print("Account not found. Sign up first")


# signup(
#     input("Choose a username : ").casefold(),
#     input("Choose a password : ")
# )

signin()
