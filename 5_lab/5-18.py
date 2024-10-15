import csv

datafile = open('./large_toy_inventory.csv', encoding="utf8")
datareader = list(csv.DictReader(datafile, delimiter=','))

Manu = 'Lego'
results = []

for i in datareader:
    if i['Manufacturer'] == Manu:
        results.append(i)
datafile.close()

with open('./toy_inventory_res.csv', 'w', newline='') as file:
    field_name = results[0].keys()
    writer = csv.DictWriter(file, fieldnames=field_name)
    writer.writeheader()
    writer.writerows(results)