from datetime import datetime

date = [int(i) for i in (str(datetime.now().date())).split("-")]
date[0] -= 25

filename = "Programmers.txt"
data_file = open("./needed_data.txt", "w")

try:
    with open("./" + filename, 'r') as file:
        for i in file.readlines():
            birth_date = [int(j) for j in i.split()[5].split('.')]
            if birth_date[0] > date[0]:
                data_file.write(i)
            elif birth_date[0] == date[0] and birth_date[1] < date[1]:
                data_file.write(i + '\n')
            elif birth_date[0] == date[0] and birth_date[1] < date[1] and birth_date[1] == date[1] and birth_date[2] < date[2]:
                data_file.write(i + '\n')
except:
    print('No such file')
data_file.close()
