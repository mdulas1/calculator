first_num = float(input("first num"))
second_num = float(input("second num"))
operation = input("operators (e.g add/plus,sub/minus, mul/times,div/seg)")

# tuple data type
operations = (operation.lower(),first_num,second_num)

match operations:
    case ("add",x,y) | ("plus",x,y):
        print("result",x+y)
    case ("sub",x,y) | ("minus",x,y):
        print("result",x-y)
    case ("mul",x,y) | ("times",x,y):
        print("result",x*y)
    case ("div",x,y) | ("seg",x,y):
        if second_num == 0:
            print("error division")
            exit()
        print("result",x/y)
    case _:
        print("Invalid operation")

