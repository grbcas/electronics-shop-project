from src.item import *


class Phone(Item):
	def __init__(self, name: str, price: int | float, quantity: int, number_of_sim: int):
		super().__init__(name, price, quantity)
		self.number_of_sim = number_of_sim

	@property
	def number_of_sim(self):
		print('getter number_of_sim')
		return self.__number_of_sim

	@number_of_sim.setter
	def number_of_sim(self, number_of_sim):
		self.validate_number_of_sim(number_of_sim)
		self.__number_of_sim = number_of_sim

	@classmethod
	def validate_number_of_sim(cls, number_of_sim):
		if number_of_sim < 1:
			raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

	def __repr__(self):
		print(self.number_of_sim)
		return f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'

	def __str__(self):
		return f'{self.name}'


if __name__ == '__main__':
	phone1 = Phone("iPhone 14", 120_000, 5, 0)
	item1 = Item("Смартфон", 10000, 20)
	# phone1.number_of_sim = 0
	print('number_of_sim', phone1.number_of_sim)
	print(phone1.__repr__())
	print(item1 + phone1)
	# Phone("iPhone 14", 120_000, 5, 0)