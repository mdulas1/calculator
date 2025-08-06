number =int( input("enter number from (1 to 7)\n"))
# if number > 1 and number < 8: #   print(f"day{number} is ")

match number:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 1:
        print("saturday")

    case _:
        print("invalid")

