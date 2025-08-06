first_number = float(input("First number:"))
second_number = float(input("Second number:"))
operator = input("enter operator:(+,-,*,/)")
if operator == "+":
    result = first_number + second_number
    print("sum",result)
elif operator == "-":
    result = first_number - second_number
    print("result",result)
elif operator == "*":
    result = first_number * second_number
    print(result)
elif operator == "/":
    if second_number == 0:
        print("zero division error")
    else:
        print("result",first_number /second_number)




