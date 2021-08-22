# Усовершенствовать родительский класс таким образом,
# чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    _name = 'A'
    _price = 10


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(ItemDiscount._name, ItemDiscount._price)
        print(self._name, self._price)  # идентичны, тк дочерний класс наследует все атрибуты и методы родит.класса.


inst = ItemDiscountReport()
inst.get_parent_data()