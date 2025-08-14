students = {
        "zainab":{"department":"cs","score":[7,22,55]},
        "emeka":{"department":"biology","score":[7,4,55]},
        "aisha":{"department":"hausa","score":[7,22,11]},
        "peter":{"department":"math","score":[7,22,30]},
        "tulo":{"department":"english","score":[7,20,55]},
        "grace":{"department":"physics","score":[10,19,20]},
        "basma":{"department":"public health","score":[14,17,20]},
        "amina":{"department":"zoology","score":[15,10,17]}

}

total_score = []
total_avg = []
for key,value in students.items():
    print(key,value)

total = sum(students[students]["score"])
total_score.append(
total)
print(total)


