from collections import deque

from src.item import *


class MixinLanguage:

	_languages = deque(('EN', 'RU'))
	_language: str = 'EN'

	def change_lang(self):
		self._languages.rotate()
		self._language = self._languages[0]
		return self


class Keyboard(MixinLanguage, Item):

	@property
	def language(self):
		return self._language


if __name__ == '__main__':
	kb = Keyboard('Dark Project KD87A', 9600, 5)
	assert str(kb) == "Dark Project KD87A"
	#
	assert str(kb.language) == "EN"
	#
	kb.change_lang()
	assert str(kb.language) == "RU"

	# Сделали RU -> EN -> RU
	kb.change_lang().change_lang()
	assert str(kb.language) == "RU"

	# kb.language = 'CH'
	# # AttributeError: property 'language' of 'KeyBoard' object has no setter
	print(kb.language)
	print(kb.__dict__)
