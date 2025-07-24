# simple program to act as a calculator
first_number = float(input("enter first_number here\n >>>"))
operator = input("enter operators (+,-,*,/): \n>>> ")
second_number  = float(input("enter your second_number here\n>>>"))


if operator == "+":
     print(first_number + second_number)

elif operator == "-":
     print(first_number - second_number)

elif operator =="*":
     print(first_number * second_number)
elif operator == "/":
     if second_number != 0:
          print(first_number // second_number)
     else:
         print("math error cannot divide by zero")
else:
    print("invalid oprator")



'''
# simple program to act as a calculator
first_number = float(input("Enter first number here\n>>> "))
second_number = float(input("Enter your second number here\n>>> "))
operator = input("Enter operator (+, -, *, /):\n>>> ")

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("Math error: Division by zero")
else:
    print("Invalid operator")

'''
