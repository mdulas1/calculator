# calculator history
history = []
history.append('''
===========================
|simple calculator history|
===========================
               ''')
print("addition")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
total = num1 + num2
result = f"{num1} + {num2} = {total}"
print(result)
history.append(result)

print("subtraction")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
total = num1 - num2
result = f"{num1} - {num2} = {total}"
print(result)
history.append(result)

print("multiplication")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
total = num1 * num2
result = f"{num1} x {num2} = {total}"
print(result)
history.append(result)
print("division")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
total = num1 // num2
result = f"{num1} / {num2} = {total}"
print(result)
history.append(result)
print(history[0])
print(history[1])
print(history[2])
print(history[3])
print(history[4])
