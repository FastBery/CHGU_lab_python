class InventoryItem:
    def __init__(self, a = 'NoData', n = 0, s = 0):
        if n < 0 or s < 0:
            raise Exception('Value must be positive')
        self.amount = n
        self.name = a
        self.price = s

    def add(self, n = 0):
        if n >= 0:
            self.amount += n
        else:
            raise Exception('Value must be positive')

    def take(self, n = 0):
        if self.amount >= n:
            self.amount -= n
        else:
            raise Exception(ValueError, 'Big Number')

    def changeprice(self, pric = None):
        if pric == None:
            return
        if pric >= 0:
            self.price = pric
        else:
            raise Exception('Value must be positive')
        
    def __str__(self):
        send = 'Name: ' + str(self.name) +'\n' \
        + 'Amount: ' + str(self.amount) + '\n'\
         + 'Price: ' + str(self.price)
        return send

item = InventoryItem('Lego', 20, 25)
# item.add(2)
# item.take(3)
# item.changeprice()
print(item)

