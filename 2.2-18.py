filename = 'text_for_2_lab'
dictionary = dict()
try:
    with open('./' + filename + '.txt', 'r') as file:
        text = file.read()
        for i in text:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    with open('./' + 'symbols' + '.txt', 'w') as file:
        file.writelines(i for i in dictionary.keys())
    print(dictionary)
except:
    print('No such file')