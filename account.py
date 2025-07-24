# account statement
password =12345678
security =int(input("enter your password\n>>"))
first_name = "John"
surname = "Ali"
last_name = "Farfa"

while True:
    if password == security:
        print("welcome", last_name,first_name)
        break
    else:
        print("try again!")
        break
        
account_number = "1023567813"
first = account_number[0]
last = account_number[-1]
length = len(account_number) -4
stars = length * "*"
bank_account = first+stars+last

account_balance ='100000'
deposit = input("Deposit here:")
new_account_balance = bank_account + deposit
print("your account",bank_account, "credit with amount of ₦:",deposit, "successfuly")
print("your new balance is ₦:",new_account_balance)
withdraw = input("Withdraw here:")
new_balance = new_account_balance - withdraw
print("your account ",bank_account,"debited with amount of ₦:",withdraw, "successfuly") 
print("your remaining balance is ₦:",new_balance,)



