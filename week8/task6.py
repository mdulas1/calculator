for num in range(1,201):
    if num % 2 == 0:
        if num >= 60 and num <= 70:
            num += 1
            continue
        print(num)
