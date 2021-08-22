# Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно.
# Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
# а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.

class ItemDiscount:
    _name = 'A'
    _price = 10

    def get_new_price(self, price, discount=0.0):
        self._price = price
        self.discount = discount
        print('New price:', self._price - (self._price * self.discount), self.__class__)


class ItemDiscountReport(ItemDiscount):
    pass


class ItemDiscountReport_1(ItemDiscountReport):
    def get_info(self):
        print(self._name)


class ItemDiscountReport_2(ItemDiscountReport):
    def get_info(self):
        print(self._price)


inst = ItemDiscountReport_1()
inst.get_info()

inst = ItemDiscountReport_2()
inst.get_info()
