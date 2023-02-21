"""
def oddCalc(a,b):
    result = a + (2*b)
    if result > 9:
        result /= 2
    return result

x = oddCalc(7,5)
print(x)

print(oddCalc(7,5))

def add(a,b):
    return a+b

def bad(a):
    print(a)

bad("It's morning.")

x = oddCalc(7,5)

"""


def makeFullName(firstName, lastName):
    fullName = firstName + ' ' + lastName
    return fullName


print("Hello " + makeFullName('Bob', 'Smith'))

fn = makeFullName('Bob', 'Smith')
print('Hello', fn)


def reassign(num1):
    num1 = 2


num2 = 1
print(reassign(num2))
