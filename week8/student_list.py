# declaring a tuple

'''
1. immutable
2. heterogenous data
3. dost not support update by default
() or tuple()

fruits = ["Mango","kiwi","orange"]
# multiple data types
multiple_data  = (45737,"Tom","1998/9/20","Male","Berom","AA","O+",fruits)
print(multiple_data[-1][-3])

bio  = (45737,"Tom","1998/9/20","Male","Berom","AA","O+")
print(bio)
name = (18,)
print(type(name))
'''

# declaring 5 tuples

data_1 = ("name","age","gender","height","width")
data_2 = (1,2,3,4,5)
data_3 = (1.0,7.0,6.5,3.8,2.1)
data_4 = []
data_5 = tuple()
data_6 = dict(zip(data_1,data_2))
items = data_6.clear()


# Datatype e.g list, tuple, set, dict

students = ("amos","ayuba","tanimu","ibrahim","abigel","rita","fatima")
scores = (17,18,19,14,20,9)
result = dict(zip(students,scores))


new = {"jibrin","mangu","oklo","jos","lucky","abuja"}
new_set = list(new)
new_set.remove("mangu")
new_set.remove("jos")
new_set.remove("abuja")
new_set.append("stanly")
new_set.append("james")
new_set.append("aduku")
converting = set(new_set)
print(type(converting))

history = []
student_bio = {}
student_bio['name'] = "Tom Jerry"
student_bio['age'] = 20
student_bio['gender'] = "male"
student_bio['matric'] = "UJ/2018/CS/0123"
student_bio['course'] = 'CSC126'
student_bio['department'] = "computer science"
student_bio["faculty"] = "computing"
student_bio["level"] = 100
student_bio["course"] = "CSC216"
history.append(student_bio)
print(history)
print(student_bio["course"])
