student = {"student":{"name":"marry","score":3,"level":"200l"}}
student["student"]["score"] += 30
student["student"]["level"] = "300l"
student.update({"age":12,"gender":{"joy": "female", "musa": "male"},"state":"plateau"})
student["gender"]["joy"] = "male"
student["gender"]["musa"] = "female"
student["state"] = "kaduna"
student["age"] += 3
student["townname"] = "j-town"

print(student)
