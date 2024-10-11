N = int(input())
files = {}
for j in range(N):
    string = [i for i in input().split()]
    files[string[0]] = string[1::]
    #print(string)
N = int(input())
for j in range(N):
    command, file = [i for i in input().split()]
    if command=="read":
        print('OK') if 'R' in files[file] else print("Access denied")    
    elif command=="write":
        print('OK') if 'W' in files[file] else print("Access denied")    
    else:
        print('OK') if 'X' in files[file] else print("Access denied")   

