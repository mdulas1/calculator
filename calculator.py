class Calculator:
    def addition (self,x,y):

       return x+y
   
    def subtraction(self,x,y):

       return x-y

    def multiplication(self,x,y):

       return x*y

    def division(self,x,y):


       return x/y if y != 0 else "can not divide by zero"
test = Calculator()

print(test.addition(2,5))
x = int(input("enter first operand:\n>>>"))
y = int(input("enter second operand:\n>>>"))
operator = input("enter the operator sign:\n>>>")
if operator == "+":
        print(test.addition(x,y))
elif operator == "-":
        print(test.subtration(x,y))
elif  operator == "*":
        print(test.multiplication(x,y))
elif operator == "/":
        print(test.division(x,y))
else:
        print("invalid operator")
