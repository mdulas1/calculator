# this python script acts as a micro-wave
import time
print('''
****************
Cohort III Mircro-wave App
*******************
1.open the Mircro-wave
2.Put the Rice
3.set time ''')
customer = {}
name=input("enter your name : \n>>>")
time_to_micro_wave = input("Duration: \n>>>")
customer["name"] = name
convert_to_int=float(time_to_micro_wave)
customer["duration"] = convert_to_int
price_to_pay = convert_to_int * 1000
customer["amount"]= price_to_pay
print(" you are charge:₦ ", price_to_pay, "only")
print("your rice will be ready in  {} min(s) {}".format( convert_to_int, name))
print("4.I will let you know when it is ready...")
print(customer)
minutes_in_seconds =60
time.sleep(convert_to_int * minutes_in_seconds)
print("5.your food is ready")
