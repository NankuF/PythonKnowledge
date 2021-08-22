#  Реализовать возможность переустановки значения цены товара.
#  Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
#  Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
#  (функция, отвечающая за отображение информации о товаре в одной строке).

class ItemDiscount:
    _name = 'A'
    _price = 10

    def get_new_price(self, price):
        self._price = price
        print('New price:', self._price, self.__class__)


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(ItemDiscount._name, ItemDiscount._price)
        print(self._name, self._price)  # идентичны, тк дочерний класс наследует все атрибуты и методы родит.класса.


a = ItemDiscount()
a.get_new_price(25)

inst = ItemDiscountReport()
inst.get_parent_data()
inst.get_new_price(20)
