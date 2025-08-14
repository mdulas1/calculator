#ploting in python programming

'''
from matplotlib .pyplot import *
x = [1,2,3,4,5,6,7,8,9,10]
y = [5,2,4,4,8,7,4,8,10,9]
plot(x,y)
xlabel('Time (s)')
ylabel('Temperature (degC)')
show()

# array in python
dictionary = {}
dictionary["name"] = input("enter your name:")
dictionary["age"] = input("enter your age:")
dictionary["gender"] = input("enter your gender:")
dictionary["village"] = input(" enter your village:")
print(dictionary)

name = input("your name here:")
age = input("your age:")
gender = input("enter your gender:")
town = input("enter your town name here")
print(f'{name}{age}{gender}{town}')

my_bio = input("(your bio):please insert chracters from (0-150)\n>>>");
print(len(my_bio));
print(my_bio[:20]);
print(my_bio[20:]);
print(my_bio[0]);
print(my_bio[-1]);
print(my_bio[::]);
my_bio.sort()

start = int(input("enter a starting number:"))
stop = int(input("enter a stopping number:"))
step = int(input("how many steps you want your number to begin:"))

for i in range(start,stop,step):
    print(i)
'''
# using for loop to find the sum of a numbers

data = [1,4,6,8,9,0]
sum = 0

#find the sum of all the numbers

for x in data:
    sum = sum + x
print(sum)

#find the mean or average of all the numbers

N = len(data)
print(N)
mean = sum//N
print(mean)

numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26}
letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
new = list(numbers)
now = list(letters)
new.sort()
now.sort()
convert = dict(zip(new,now))
print(convert)
