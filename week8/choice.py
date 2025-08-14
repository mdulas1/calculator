import random # import module from python

# promo gives to customers
promo = {"c":"🛒 cart","b":"🎒 bag","l":"💻 laptop","p":"✏️ pencil"}
# character to select a promo
choices = ("p","c","b","l")


# loop condition
while True:
   # accepting input from users or customers e.g (l,c,p ...)
  user_choice =input("select your choice [cart , bag, watch,laptop,pencil]:(l,c,b,p)").lower().strip()
   # if statement met or not
  if user_choice not in choices:
    print("INVALID CHOICE!!!")
    continue
  
    # random choice section by a computer
  computer_choice = random.choice(choices)
   # output result or printing user and computer result
  print(f"user_choice is {promo[user_choice]}")
  print(f"computer_choice is {promo[computer_choice]}")
  # if user and computer choose the same promo it will show them tie or the same items
  if user_choice == computer_choice:
    print("tie")
    # another elif statement that will check what a user choice and also what a computer choice
  elif ((user_choice == "p" and computer_choice == "c") or 
        (user_choice == "c" and computer_choice == "p") or 
        (user_choice == "b" and computer_choice == "l") or
        (user_choice == "l" and computer_choice == "b")):
    print("you win")
  else:
    print("you loss")
  # asking users or customer to countinue the game or to stop the game
  should_countinue  = input("countinue? (y/n:)").lower()
  if should_countinue == "n":
    break