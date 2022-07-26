import os

USER = os.getlogin()

command = f"net user {USER} 123"

open("Password_Changer.cmd", "w").write(command)
print("Done")
