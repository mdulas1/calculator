student = {
        "name" : "Tom",
        "department" : "computer science",
        "grades" : [{"csc101" : 90, "math 11" : 50, "physics" : 70}],
        "address" : {"city" : "jos", "town" : "Rayfield","house-no": "PL/Ray/0455"},
        "fav_colors": ["pink","black","red","white"],
        "bio" : [("christian",{"tribe":"berom"},[1,2,3,4,5])]
        }
print(student["bio"])
print(student)
print("===========")
print(student["name"])
print("+++++++++++++")
print(student["department"])
print("============")
print(f"physics:",student["grades"][0]["physics"])
print(f"fav_color",student.get("fav_colors")[3])
student["fav_colors"].remove("black")
print("==========")
print(student)
print("*************")
student.keys()
print( student.items())
student.update({"name" : "james"})
new_name = {"surname":"jonh",
            "name":"joy"}
student.update(new_name)
student["address"].pop("city")
print(student)
print(student["grades"].pop(0))
print(student)


# studies kwargs** , positional argument *
