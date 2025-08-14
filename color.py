'''
first_favorite_color = "Blue"
second_favorite_color = "Black"
third_favorite_color = "Pink"
fourth_favorite_color = "Gray"
fifth_favorite_color = "Green"

# countries
country1 = "Australia"
country2 = "Nigeria"
country3 = "Malawi"
country4 = "USA"
country5 = "Iran"
country6 = "Iserael"
country7 = "Russia"
country8 = "Ghana"

# countrie using list bracket
countries = ["Australia","Nigeria","Malawi","USA","Iran","Iserael","Ghana","Russia"]
print(countries)
print(countries[-1])
print(len(countries))
'''

password = input("enter your password here")
first = password[0]
last = password[-1]
length = len(password) - 2
stars = "*" * length 
secret_pass = first+stars+last
print(secret_pass)

email = input("enter your email here")
first_name = email[:5]
last_name = email[-5:]
length = len(email) - 10
stars = "*" * length
hidden_mail = first_name+stars+last_name
print(hidden_mail)
