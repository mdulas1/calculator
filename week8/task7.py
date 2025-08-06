discount =0
amount = int(input("enter amount"))
if amount >= 50000:
    discount += 20
if amount >= 30000 and amount <= 50000:
    discount += 10
if amount >= 10000 and amount <= 30000:
    discount += 5
else:
    print(f"the amount you entered is:{amount}")
total_discount = discount/100*amount
final1 = amount - total_discount
print(f"the total_discount is :{total_discount}")

print(f"the final amount is :{final1}")
