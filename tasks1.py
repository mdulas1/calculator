# week 7 tasks
# creating a list of movies, numbers and name, gender ...

list_of_my_favorite_movie =["marlin","zamani","twins worrior","the one","the karete kid"]
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
my_info = ["name:jibrin",24,False,"gender:male",3.7,"green"]
provision =["sugar","maggi","pepe","onion","gari","knife"]
print(list_of_my_favorite_movie)
print(list_of_numbers)
print(my_info)
print(provision)

android = ["Samsung","Tecno","Itel","Redmi","Oppo"]
ios = ["11-pro-max","15-pro-max","Xr","16-plus","7-plus"]
phones =[android,ios]
print(phones)


# extracting the code variable into pieces
code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-    ", "n", " ", "W", "@", "r", "d", "o", "#"]
print("{}{}{}{}{}".format(code[1],code[2],code[4],code[4],code[8]))
w =code[-6]
o = code[-2]
r = code[-4]
l = code[-14]
d = code[-3]
print(f"{w}{o}{r}{l}{d}")
print(code[::-1]) # reverse the text

# extract the grid using their index
grid = [
        ["The", "sky", "is"],
        ["full","of","stars"],
        ["shining","brigth","tonight"]

        ]
print("{} {}".format(grid[0][0],grid[0][1]))
print("{} {} are {}".format(grid[0][0],grid[1][2],grid[2][0]))
print(grid[1][::-1])

playlist = ["Song A", "Song B", "Song C"]
print(playlist)
playlist[1] ="Song D"
print(playlist)
playlist.append("Song E")
print(playlist)
print(f" intro {playlist}")


desks = []

seat1 = input("student1")
seat2 = input("student2")
seat3 = input("student3")
desks.append(seat1)
desks.append(seat2)
desks.append(seat3)
print(desks)
desks [1]= input("enter the name of a new student that wiil replace seat2")
add_seat = input("enter the name of a student to be seated b/t first and second seat")
desks.insert(1,add_seat)
print(desks)

countries =["spain","malawi","iran","usa"]
details = countries[0:3]
print(type(details))
country1 , country2 = countries[2:4]
print(country1,country2)

account = [
           ["1001","Joy","Saving",1500],
           ["1002","David","Current",2000],
           ["1003", "Ruth","Saving",1800],
           ["1004", "John", "Current",3000]

           ]

account.remove(account[1])
Ruth_account = account[1]
print(Ruth_account)
account_type = Ruth_account[1:3]
print(account_type)
joy_account = account[0][1:3]
print(joy_account)

account[2][2] = "Saving"
account[0][2] = "Current"
account[0].append("First_bank")
account[1].append("Union_bank")
account[2 ].append("Jaiz_bank")

users = account[:4]
print(users)
joy = account[0][1]
ruth = account[1][1]
john = account[2][1]
k = account[1]
print(k)
print("{}-{}-{}".format(joy,ruth,john))

