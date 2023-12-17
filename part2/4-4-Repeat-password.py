pwd = input("Password: ")

while True:
    repeatPwd = input("Repeat password: ")

    if pwd == repeatPwd:
        break

    print("They do not match!")

print("User account created!")