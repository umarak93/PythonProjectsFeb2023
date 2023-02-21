
import TaxCalculator as TC

amount = int(input("Enter your income:"))
print(TC.getIncomeTax(amount))


"""
salary = int(input("Enter your income:"))
def getIncomeTax():
    if salary <= 11850:
        print("You take home: ", salary)
    elif salary <= 34500:
        twentyper = salary * 0.2
        print("You take home: ", salary - twentyper)
    elif salary <= 150000:
        fourtyper = salary * 0.4
        print("You take home: ", salary - fourtyper)
    else:
        fourtyfive = salary * 0.45
        print("You take home: ", salary - fourtyfive)
    return

print(getIncomeTax())
"""
