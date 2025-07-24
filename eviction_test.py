# Question 1
# social media biodata
bio = input("please write about your bio:")
print(bio[:20])
print(bio[20:])
print(len(bio[20:]))

# Question 2
# food payment method by some friends
friends = int(input("number of friends"))
amount = float(input("enter amount"))
calculate = amount // friends
print(f" your total amount is {amount} and you are to pay {calculate} per each person")

# Question 3
# program to ask users how many number of movie he watched
movie = input("enter your favorite movie")
times_to_watch = int(input("enter number of times:"))
print(f" i have watched the {movie} movie  {times_to_watch}.times")
print(movie.upper())
print(movie[3:])

# Question 4
# program to calculate fitness
user_name = input("what is your name?\n>>")
monday_fitness = int(input("enter the number of steps you took in monday:"))
tuesday_fitness = int(input("enter the number of steps you took in tuesday:"))
wednesday_fitness = int(input("enter the number of steps you took in wednesday:"))
step = monday_fitness + tuesday_fitness + wednesday_fitness
average = step // 72
print(f"{user_name} on monday you took {monday_fitness:,} step and tuesday you took {tuesday_fitness:,} steps  and wednesday you took {wednesday_fitness:,} steps the total steps is {step:,} in whole days")

# Question 5
# how to create a hiden password in python programming
password = input("enter password")
first =password[0]
last = password[-1]
lenth = len(password)
visible_char = 2
num_of_stars = lenth - visible_char
stars = "*" * num_of_stars
print(f"{first}{stars}{last}")
print(lenth)
