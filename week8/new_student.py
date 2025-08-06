student1 = {
        "name" : "Tom",
        "university" : "Uj",
        "department" : "cs"
        }
print(student1)
student2 = student1 
student2["name"] = "kelvin"
print(student2)
student3 = student2.copy()
student3["name"] = "ibrahim"
print(student3)
student4 = student1.copy()
student4["name"] = "dimka"
print(student4)
history = []
history.append(student1)
history.append(student2)
history.append(student3)
history.append(student4)
print(history)
