from src.item import *


class Keyboard(Item):
	def __init__(self, name: str, price: int | float, quantity: int, language: str):
		super().__init__(name, price, quantity)
		self.language = language

	def change_lang(self):
		pass
