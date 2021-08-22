# Проверить механизм наследования в Python.
# Для этого создать два класса.
# Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
# Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
# отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.

class ItemDiscount:
    name = 'A'
    price = 10


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(ItemDiscount.name, ItemDiscount.price)
        print(self.name, self.price)  # идентичны, тк дочерний класс наследует все атрибуты и методы родит.класса.


inst = ItemDiscountReport()
inst.get_parent_data()
