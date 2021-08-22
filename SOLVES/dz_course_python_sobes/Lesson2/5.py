#  Реализовать расчет цены товара со скидкой.
#  Величина скидки должна передаваться в качестве аргумента в дочерний класс.
#  Выполнить перегрузку методов конструктора дочернего класса
#  (метод init, в который должна передаваться переменная — скидка),
#  и перегрузку метода str дочернего класса.
#  В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
#  Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
#  (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:
    _name = 'A'
    _price = 10

    def __init__(self, discount):
        self.discount = discount

    def get_new_price(self, price, discount=0.0):
        self._price = price
        self.discount = discount
        print('New price:', self._price - (self._price * self.discount), self.__class__)


class ItemDiscountReport(ItemDiscount):
    def __init__(self, discount):
        super().__init__(discount)

    def __str__(self):
        return self.get_new_price

    def get_parent_data(self):
        print(ItemDiscount._name, ItemDiscount._price)
        print(self._name, self._price)  # идентичны, тк дочерний класс наследует все атрибуты и методы родит.класса.


a = ItemDiscount(10)
a.get_new_price(25)

inst = ItemDiscountReport(15)
inst.get_new_price(30, 0.10)
