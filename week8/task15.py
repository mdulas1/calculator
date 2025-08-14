'''
name = input("enter your name\n")
score = float(input("enter score\n"))
data = {"name":name,"score":score}
match data:
    case {"name":x,"score":y}:
        if score >= 70 and score <= 100:
            print(x,"A")
        elif score == 60:
            print(x,"B")
        elif score > 100:
            print("invalid range of scores plase try another number from (0 - 100)")
        else:
            print(x,"fail")
    case _:
        print("invalid input")
print(data)
'''
passengers = int(input("enter the number of passengers:"))
amount_per = float(input("amount per each:"))
if amount_per <= 0:
    print("Ivalid amount\n try again")
    exit()
cost_amount = 200
total_price = passengers *cost_amount
amount_per -= total_price
print(f"my total money is:{total_price}")
print(f"your remaining balance is: {amount_per}")
