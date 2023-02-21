str = "bob smith"

print(str.capitalize())
print(str.title())
print(str.replace(' ','_'))
print(str.title().replace(' ','_'))

cities = "london,brimingham,leeds,manchester,bristol"
cityList = cities.split(',')
print(cityList)
city = input('Please enter a city:')

if city.lower() in cityList:
    print('Your city is in the list!')

data = [1,3,5,7,9,11,13,15]
print(data[1:5])

