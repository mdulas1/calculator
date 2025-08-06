# validation
balance = 20000
user_amount = input("Amount to withdraw:\n")
amount = int(user_amount)
if amount <= 0:
    print("Invalid amount")
elif amount % 500 != 0:
    print("invalid amount to withdraw")
elif amount > 10000:
    print("Daily limit exceeded")
elif amount > balance:
    print("Insufficient balance")
else:

    balance = 


