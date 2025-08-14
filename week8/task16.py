'''
# program to calculate factorial of a number
number = int(input("enter number"))
I = 1
factorial = 1
while I <= number:
    factorial *= I
    I += 1 
print(factorial)
'''
'''
# number cheking system using python

num1 = int( input("Enter num1:"))
num2 = int( input("enter num2:"))
if num1 > num2:
    print(f"{num1} is greather than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")
else:

    print(f"{num1} is less than {num2}")
'''
# This technique is known as Ternary Operators, or Conditional Expressions.
a = 300
b = 30
print(f"{a} > {b}") if a > b else print(f"{a} == {b}") if a == b else print(f"{a} < {b}")

c = 40
if c > 10:
    print("above 10")
    if c > 20:
        print("above 20")
        if c > 30:
            print("above 30")
            if c == 40:
                print("thase number")

day = 4
match day:
    case 1 | 2 | 3 |4 |5:
        print("working day")
    case 6|7:
        print("weekend day")
    case _:
        print("Invalid input")

num = 1
while num < 11:
    print(f"{num} * {num} = {num*num}")
    num +=1

fruits = ["banana","apple","mango"]
for x in fruits:
    print(x)

[print(x) for x in ["banana","apple","mango"]]

n = 5
i = 1
f = 1
while i <= n:
    f *=i
    i += 1
    print(f)
