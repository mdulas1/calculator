customer = []
print("""

1. onboard customer
2. withdraw cash
3. add cash
4. transfer
5. change pin
    """)
automatic_id = 1
user_input = int(input("select an operation:"))
if user_input >=1 and user_input <= 5:
    if user_input == 1:
        user_name = input("enter user name:")
        user_amount = float(input("enter amount:"))
        user_pin = input("enter your pin:")
        if len(user_pin) == 4:
            new_customer = {
                    "name": user_name,
                    "amount": user_amount,
                    "pin":int( user_pin),
                    "auto_Id": automatic_id

                    }
            automatic_id +=1
            customer.append(new_customer)
        else:
            print("invalid pin length")
    if user_pin == 2:

else:
    print("invalid selected operation")
print(customer)
    

