# program to acts as micro-wave
import time
print('''
1. open the micro-wave
2. put your food
3. set time
''')
micro_wave = input("press start to open! \n >>>")
if micro_wave == "start":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("start your cooking!")
else:
        print("try again")
my_home = {}
name = input("enter your name here:\n>>>")
my_home ["name:"]=name
cooking_type = input("enter name of food \n >>>")
my_home["types_of_food"]= cooking_type
print("you wi ll be charging at ₦1000 per min")
time_to_finish = int(input("set time"))
charging = time_to_finish * 1000
my_home["charges:₦ "]= charging
my_home["duration:"]=time_to_finish
convert= time_to_finish * 60

print("your {} is cooking now".format(cooking_type))
while  convert > 0:
     time.sleep(1)
     print(convert)
     convert = convert - 1
print("your {} is ready".format(cooking_type))
print("your {} is cooked at {} (second/minutes) ".format(cooking_type,time_to_finish))
print(my_home)
