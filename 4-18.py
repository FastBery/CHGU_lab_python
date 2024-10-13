filename = 'matrix.txt'
matrix = []
new_matrix = open('./new_matrix.txt', 'w+')
try:
    with open('./' + filename) as file:
        for line in file:
            matrix.append([float(i) for i in line.split()])
        for i in matrix:
            for j in i:
                if j%2 != 0:
                    new_matrix.write(str(j+10) + ' ')
                else:
                    new_matrix.write(str(j/4) + ' ')
            new_matrix.write('\n')
except:
    print('no file')

new_matrix.close()

# with open('./new_matrix.txt', 'r') as file:
#     lines = str(file.readlines()).strip('\n')
#     print(lines)