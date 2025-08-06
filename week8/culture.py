('tribe', 'language', 'food','festival',('cloth', "greeting"))
cultures = [
        ("Ngas","Ngas","bwan","Pusdung",("Funkaya","yala")),
        ("Berom","Berom","Gwote","Nzem Berom",("Ashui","shou")),
        ("Afizere","Izere","Tuwon Masara","Izere day",("Angrari","Mavo"))


        ]
greeting = cultures[1][-1][-1]
print(greeting)
print(f"the {cultures[0][0]} people wear {cultures[0][-1][-2]} and eat {cultures[0][2]}")
item1,item2,*items = cultures[2][3], cultures[2][2]
print(item1)
print(item2)

change = cultures[1]
print(change)
change = list(change)
change[0] = "Hausa"
change[1] = "Hausawa"
change[2] = "Dambu"
change[3] = "Aragungun festival"
change1 = tuple(change)
convert = change1
convert = list(convert)
print(convert)
convert[-1] = "Inakwana","Lafiya"
print(convert)

convert = tuple(convert)
print(type(convert))
bio = ("Tom","1998/9/20","male","berom")
print(bio)
bio = list(bio)
bio[0] = "Jerry"
bio = tuple(bio)
print(bio) 
