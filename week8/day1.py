'''
18-25 : regular
26- 35 : vip
36-40: vvip
'''
age = int(input("Age:"))
if age >=18 and age <= 25:
    print("regular")
if age >=26 and age <=35:
    print("vip")
if age >=36 and age <= 40:
    print("vvip")
if age < 18 and age > 40:
    print("no place for you")
