'''
number = "zxascvqwernbmnrtuihjpokjgy"
n = number[10:11]
i = number[17:18]
g = number[-2]
e = number[8:9]
r = number[9:10]
i = number[17:18]
a = number[2:3]
i = number[17:18]
s = number[3:4]
m = number[-14]
y = number[-1]
c = number[4:5]
o = number[-5]
u = number[-10]
n = number[10:11]
t = number[-11]
r = number[9:10]
y = number[-1]
print(f"{n}{i}{g}{e}{r}{i}{a} {i}{s} {m}{y} {c}{o}{u}{n}{t}{r}{y}")
a = "hello world!"
print(a)
print(a[1])
print(a[2:5])
print(len(a) * 2)
print(a.lower())
print(a.upper())
print(a.split())
'''
get_password = input("enter password:\n>>")
first = get_password[0]
last = get_password[-1]
length = len(get_password)
visible = 2
number_of_stars = length - visible
stars = "*" * number_of_stars
print(f"{first}{stars}{last}")
