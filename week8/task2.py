'''
import random
students = []
for i in range(1,100):
    students.append({"id":i,"name":f'Student{i}',"score":random.randint(0,100)})

good_performers = []
middle_performers = []
bad_performers = []

for student in students:
    student_data = {student["id"]: ({student["name"],student["score"]})}

    if student["score"] >= 70:
        good_performers.append(student_data)
    elif 50  <= student["score"]  < 70:
        middle_performers.append(student_data)
    else:
        bad_performers.append(student)
print(f'total of hihger performers students:',len(good_performers))
print(f'total of average performers students:',len(middle_performers))
print(f'total of lower performers students:',len(bad_performers))

print("========= Group A ==========")
print(good_performers)
print("======== Group B ==========")
print(middle_performers)
print("======== Group C =========")
print(bad_performers)
'''
print(not 4 == 4 )
print(1 == 1 and 2 >1)

a = []
b = a
c = b
c.append("fruit")
b.append("phones")
a.append("laptops")
print(c)


