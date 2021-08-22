# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

class ItemDiscount:
    _name = 'A'
    _price = 10


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(ItemDiscount.name, ItemDiscount.price)
        print(self.name, self.price)  # идентичны, тк дочерний класс наследует все атрибуты и методы родит.класса.


inst = ItemDiscountReport()
inst.get_parent_data()