'''
Assignment Questions
 Question 1
 '''
my_age = 24
PI = 3.14159

magic_number = my_age * 3 + PI % 7
print("the value of magic_number is {}".format(magic_number))
print(type(magic_number))

# Question 2
secret_word = "PythonIsAmazing"
print(secret_word[:6])
print(secret_word[8:])
print(secret_word[6:8])
print(secret_word[:])
print(secret_word[::2])

# Question 3


print(secret_word[:6].upper())
print(secret_word[6:].lower())

combine1 = secret_word[:6].upper()
combine2 = secret_word[6:].lower()
print(combine1, combine2)
