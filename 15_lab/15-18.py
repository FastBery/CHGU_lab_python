import openpyxl

wb = openpyxl.load_workbook('./15_lab/18.xlsx')

sheet = wb.active

n = 0

for i in sheet.iter_rows(values_only=True):
    mul = 1
    for k in i:
        for j in str(k):
            mul *= int(j)
    if sum(i) < mul:
        n += 1

print(n)