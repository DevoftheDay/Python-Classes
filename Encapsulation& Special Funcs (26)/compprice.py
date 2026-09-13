class Computer:

    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print("SellingPrice : {}".format(self.__max_price))

    def alterPrice(self, price):
        self.__max_price = price


c = Computer()
c.sell()

c.__max_price = 1000
c.sell()

c.alterPrice(1000)
c.sell()
