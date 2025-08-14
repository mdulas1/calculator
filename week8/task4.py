# withdrawal banking system

account_balance = 10000
withdrawal_amount = float(input("enter amount you want to withdraw:"))
if withdrawal_amount % 1000 == 0:
    print("invalid amount")
    if withdrawal_amount > account_balance:
        print("insufficient fund")
    else:

          withdraw = account_balance - withdrawal_amount
          print(f" succesfully withdrawal of{withdrawal_amount}")
else:
    print("invalid amount")

count = 0
for item in range(100):
    print(item)
    # Do something with item
    count += 1
print(f"The loop executed {count} times.")
