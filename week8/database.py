print('''
      =============
      |1.login    |
      |2.register |
      |3.exit     |
      =============
      ''')
database = {
        "username":{},
        "password":{},
        "initial_amount":{},
        "is_vetified":{}
        }
command = input("select a command").lower().strip()
if command not in ["login","register","exit"]:
    print("invalid command")
elif command == "register":
    print("please fill the form below to register")
    database["username"] = input("create a user name:")
    if database["username"] in database:
        print(f"username {username} already exist")
    else:
        print("continue register")
    database["password"] = input("create password")
    database["intial_amount"] = float(input("enter amount:"))
    if database["initial_amount"] == 1500:
        print("countinue")
    else:
        print("try again")
    database["is_verified"] = False
print(database)
