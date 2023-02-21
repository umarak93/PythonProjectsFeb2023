

def getIncomeTax(salary):
    personal = 11850
    takehome = 0
    if salary <= personal:
        takehome = salary
    elif salary <= 34500:
        takehome = (salary - personal) * 0.2
    elif salary <= 150000:
        takehome = (salary - personal) * 0.4
    else:
        takehome = (salary - personal) * 0.45
    return takehome
