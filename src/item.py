from csv import DictReader
from pathlib import Path

path_to_file = Path(Path(__file__).parent, 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.validate_name(name)
        self.__name = name

    @classmethod
    def validate_name(cls, name):
        if len(name) >= 10:
            raise ValueError(f'"{name}" Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls, path_csv=path_to_file):
        cls.all.clear()
        try:
            with open(path_csv, encoding='cp1251', mode='r') as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    cls(name=row['name'], price=row['price'], quantity=row['quantity'])
            return cls.all
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {path_csv}')
        except KeyError:
            raise InstantiateCSVError(f'Файл {path_csv} поврежден ')

    @staticmethod
    def string_to_number(var):
        return int(float(var))

    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('сложение по количеству товара в магазине')
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):
    """Class error message for data corruption file"""

    def __str__(self):
        if self.args:
            return f'{self.args[0]}'
        return f'Файл поврежден'


if __name__ == '__main__':
    item = Item.instantiate_from_csv()
    print(item)
