class Mass:
    
    def __init__(self, array):
        if type(array) == list:
            if not all(isinstance(item, str) for item in array):
                raise TypeError("List must consist of str")
            if not all(len(item) == len(array[0]) for item in array):
                raise IndexError("strings must be the same size")
            self.array = array
        elif type(array) == Mass:
            self = array

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index must be integer")
        if 0 <= key <= len(self.array):
            return self.array[key]
        else:
            raise IndexError("Wrong index")

    def __str__(self):
        return str(self.array)

    def append(self, other):
        for x in other.array:
            self.array.append(x)

    def __add__(self, other):
        for x in other.array:
            self.array.append(x)
        return self
        
    def merge(self, other):
        dict = {}
        for x in self.array:
            dict[x] = 1
        for x in other.array:
            dict[x] = 1
        self.array = list(dict.keys())
        return self


array = Mass(['s', 'a', 'd','v'])
print(array)
print(array[2])
array2 = Mass(['n','b', 's', 'a'])
array3 = array2 + array
print(array3)
# array3 = array + array2

print(array.merge(array2))
print(array)

# a1 = [1,2,3]
# a2 = [4,5,6]
# a1.append(x for x in a2)
# print(a1)
