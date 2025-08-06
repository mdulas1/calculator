# match == switch
first_number = float(input("first"))
second_number = float(input("second"))
operator = input("operator(+,-,*)")

match operator:
    case "+":
        print("sum", first_number + second_number)
    case "-":
        print("result", first_number - second_number)
    case "*":
        print("result", first_number * second_number)
    case "/":
        if second_number == 0:
            print("division error")
        else:
            print("result",first_number / second_number)
    case "_":
        print("invalid operator")

