companies = []
sales = []
count = 0

with open("carSale.csv") as file:
    while True:
        count += 1
        line = file.readline().strip()
        if line == '':
            break
        if count % 2 == 1:
            companies.append(line)
        else:
            #data = []
            #data.append()
            sales.append(line.split(","))

for company in companies:
    print(company)
for sale in sales:
    print(sale)

print(sales[2][3])

