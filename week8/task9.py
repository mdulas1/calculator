jamb_score = int(input("enter your jamb score:"))
if jamb_score >=250 and jamb_score <=400:
    print("eligible for medicine")
elif jamb_score >= 200 and jamb_score <= 249:
    print("eligible for engineering or any other science course")
elif jamb_score >= 180 and jamb_score <=199:
    print("eligible for education or social science")
elif jamb_score < 180:
    print("your are not eligible for addimision in (UJ)wait for next year or change the institution of learning")
else:
    print("above our marking range")

