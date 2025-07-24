search = open("test.py", "r")
data = search.read()
print(data)
search.close()

put = open("test.py", "w")
programming = "python_programming_language"
data = put.write(programming)
print(data)
put.close()


