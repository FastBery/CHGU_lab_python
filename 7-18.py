class PhoneCall:
    def __init__(self, n = 0, s = 0):
        self.price = s
        self.minutes = n

    def summ(self):
        return self.price * self.minutes

    def __str__(self):
        string = 'Price: ' + str(self.price) + '\n' \
            + 'Minutes: ' + str(self.minutes)
        return string

call = PhoneCall(20, 0.5)

print(call)
print(call.summ())

