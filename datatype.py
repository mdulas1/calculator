# Data types
'''
str
int
bool
float
set is unique -> {}
list not unique -> []
'''

"""
customers = ['Tom','jerry','mark','val','ben','mimi','jerry','musa','ibrahim']
database = {}
database["name"] =input("enter your name here:")
database["age"] = int(input("enter your age here:"))
database["gender"] = input("enter gender here:")
print(len(database))
"""
# users bio data details
users = {}
name = input("enter your name:")
users['name'] = name
age = int(input("enter your age:"))
users['Age'] = age
hieght =float(input("enter your hieght:"))
users['Hieght'] = hieght
gender = input("enter your gender:")
users['Gender'] = gender

print("users details:{}".format(users))

people = {'Tom','Jerry','Mark','Val','Ben','mimi','Musa','Ibrahim','Jerry','Musa'}
print(people)

