# Comparison operators
'''
operand1 = 1
operand2 = 5
print(operand1 > operand2)

name1 = True
name2 = 2
print(name1 > name2)

user_age = int(input("Enter your age: "))
print(f"is {user_age} greather than or equal too 18 ?", user_age > 10)
'''
#score = float(input("enter your grade:"))
#print(f"is {score} greater than or equal too 70", score >= 70)
'''
pin = 4190
print("Welcome to our Atm")
user_pin = int(input("Enter your pin:"))
print("is the user pin correct", user_pin == pin)

phone_password =41111
user_password = int(input("Enter your password"))
check_user_password = user_password == phone_password
print("Is the user password correct",check_user_password)

num1 = 30 
num2 = 50
print((num1 > num2 ) and (num2 > num1))
user_score = int(input("Score:"))
print("should your grade be A?:",user_score >= 70 and user_score <= 100)

'''
num1 = 30 
num2 = 50
print(not(num1 > num2))
print((num1 < num2) and (num1 > num2))
print((num2 < num1) or (num1 < num2))

