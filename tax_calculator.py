# Tax calulator
income =float(input("enter your annual income:"))
tax = 0
if income < 10000:
    tax = 0
    print(f"{income:,.2f}")
elif income > 10000 or income  < 30000:
    tax_a = 1 // 100 * income
    tax = income - tax_a
    print(f"{tax:,.2f}")

elif income > 30000 or income < 70000:
    tax_a = 2 // 100 * income
    tax = income - tax_a
    print("{tax:,.2f}")
else:
    print("try again")
