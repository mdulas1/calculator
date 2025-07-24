'''
start = 1
stop = 101
for i in range(start, stop):
    print(i)
the_weather_is_good = 1
go_for_walk = 0
have_lunch = 1
if the_weather_is_good:
    go_for_walk()
have_lunch()


if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_theater()
    else:
        go_shopping()


if the_wether_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
'''
number1 = 1
number2 = 10
number3 = 15
number4 = 9

largest_number = max(number1,number2,number3,number4)
smallest_number = min(number1,number2,number3,number4)

print("the largest number is:", largest_number)
print("the smallest number is:", smallest_number)

