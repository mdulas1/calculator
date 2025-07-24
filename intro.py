# logic engine
import time

print('''
engine hint
(***************)
1.S >> start 
2.D >> drive
3.R >> reverse
4.P >> park
''')

while True:
    car_name = input("Enter your car name here\n>> ")
    command = input("S >> start engine\n>> ")
    if command == "S":
        print(car_name, "engine started")
        while True:
            print('''
Driving mode command
1.D >> drive
2.R >> reverse
3.P >> park
            ''')
            mode = input("Enter driving mode (D/R/P/H>> over-draft) or Q to quit:\n>> ")
            if mode == "D":
                for i in range(1, 4):
                    time.sleep(1)
                    print(i)
                print("Driving mode activated")
            elif mode == "R":
                for i in range(1, 4):
                    time.sleep(1)
                    print(i)
                print("Reverse mode activated")
            elif mode == "P":
                for i in range(1, 4):
                    time.sleep(1)
                    print(i)
                print("Parking mode activated")
            elif mode == "H":
                for i in range(1,4):
                    time.sleep(1)
                    print(i)
                    print("over draft mode activate")
            elif mode == "Q":
                print("Exiting driving mode.")
                break
            else:
                print("Wrong command, try again!")
    else:
        print("Wrong command, try again!")