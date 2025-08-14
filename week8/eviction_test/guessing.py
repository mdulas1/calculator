# generate a random number
import random
#loo
guess = random.randint(1,100)
count = 1
while count:
    number = int(input("enter number from (1-100)"))
    count += 1
    if number < 0 and number >0:
        print("invalid input")
    elif number < guess:
        print("too low")
    elif number > guess:
        print("too high")
    else:
        count -= 1
        print(f"congratulation you finally attempt in  {count} times ")
        break

