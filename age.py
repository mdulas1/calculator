score = float(input("enter score:"));
pass_mark = 45;
if score >= pass_mark and score <= 100:
    print("pass");
else:
    print("fail");

number = int(input('enter number to find a factorial a number:'))
initial = 1
factorial = 1
while initial <= number:
    factorial *= initial
    initial += 1
    print(factorial,"🧩🧩")

