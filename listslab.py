ages = [12, 18, 33, 84, 45, 67, 12, 82, 95, 16, 10, 23, 43, 29, 40, 34, 30, 16, 44, 69, 70, 74, 38, 65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
#print(len(ages))

#for age in ages:    # print each in new line
#    print(age)

#for age in ages:    # add 1 to each age
#    age += 1
#    print(age)


#i = 0   #used as index

#while (i < len(ages)): # add 1 to each age
#     print(ages[i]+1)
#     i += 1
filtered = []
for x in ages:
    if 65 >= x >= 16:
        filtered.append(x)





