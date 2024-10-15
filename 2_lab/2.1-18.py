import re

filename = 'text_for_2_lab'
try:
    with open('./' + filename + '.txt', "r") as file:
        strings = file.readlines()
        text = [re.sub(r'\s+', ' ',str(i)) for i in strings]

    with open('./' + filename +'_2' + '.txt', 'w') as file:
        file.writelines(i + '\n' for i in text[:-1:] )
        file.writelines(text[-1])
except:
    print('No such file')


