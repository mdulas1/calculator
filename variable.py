# names of students

first_name = "yusuf" # first_name is a variable that store first name of a user
second_name = "aliyu" # second_name is a variable that store second name of a user
'''
customers name
customer_name is a variable that store customer name
marketer_name is avariable that store marketer  name

'''


customer_name  = "you"
marketer_name = "I"

#declaretion of six vairable in two line of code.

name,user,customer = "jbrin","bobo","farhan"
student = input("enter your name")

red,yellow,black ="red","yellow","black"

print(name,user,customer,sep="*_",end=" ")
print(student)

print(f"{name} {user} {customer}")
print("{} {} {}".format(name,user,customer))
print(name + " " + user + " " + " " + customer)
print(name, user, customer)
start = 3
stop = 12
step = 3
for x in range(start, stop, step):
    print(x)
