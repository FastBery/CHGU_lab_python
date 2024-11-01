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

    @classmethod
    def forclass(cls, ):
        return cls(n)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index must be integer")
        if 0 <= key <= len(self.array):
            return self.array[key]
        else:
            raise IndexError("Wrong index")

    def __str__(self):
        return str(self.array)

    def __add__(self, other):
        for x in other.array:
            self.array.append(x)

    



array = Mass(['s', 'a', 'd','v'])
array2 = array
array3 = array + array2

print(array2)

# a1 = [1,2,3]
# a2 = [4,5,6]
# a1.append(x for x in a2)
# print(a1)
