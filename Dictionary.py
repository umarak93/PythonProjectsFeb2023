"""
mdict = {"John": 97, "Susan": 67,"Sam": 80}
pdict = {"John": 89, "Susan": 70, "Sam": 73}

for n in mdict:
    print(n, mdict[n])

alld = {"John": [97, 89], "Susan": [81, 72], "Sam": [78, 85]}
alld["Chris"] = [40, 37]
print(len(alld))
for n in alld:
    print(n, "Maths:", alld[n][0], "Physics:", alld[n][1])

mystr = "sandcastle"
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for n in mystr:
    if n in vowels:
        count += 1
print(count)

mydict = {}
mydict["car"] = "Fiesta"

print(mydict["car"])
"""
