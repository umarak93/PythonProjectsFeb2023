"""
file = open("students.txt", "r")             #"r" is for read
#line = file.readline()
line2 = file.readlines()
#line3 = file.readline()

file.close()

for line in line2:
    print(line)

#print(line)
#i didthe print(line2)
#print(line3)
"""
"""
file = open("students.txt", "r")

for line in file:
    print(line.strip())
file.close()
"""
with open("students.txt", "a") as file:          #"a" is for append
    file.write("Bob, Smith, 30, 80, 70, 60\n")
    file.write("Rob, Jones, 20, 60, 80, 90\n")
