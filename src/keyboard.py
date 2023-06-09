from src.item import *


class MixinLanguage:
	LANGS = ['EN', 'RU']

	def __init__(self, *args):
		super().__init__(*args)
		self.__language = self.LANGS[0]

	@property
	def language(self):
		return self.__language

	def change_lang(self):
		if self.language == self.LANGS[0]:
			self.__language = self.LANGS[1]
		else:
			self.__language = self.LANGS[0]
		return self


class Keyboard(MixinLanguage, Item):
	def __init__(self, *args):
		super().__init__(*args)


if __name__ == '__main__':
	kb = Keyboard('Dark Project KD87A', 9600, 5)
	assert str(kb) == "Dark Project KD87A"
	#
	assert str(kb.language) == "EN"
	#
	kb.change_lang()
	assert str(kb.language) == "RU"
	#
	# # Сделали RU -> EN -> RU
	kb.change_lang().change_lang()
	assert str(kb.language) == "RU"

	kb.language = 'CH'
	# AttributeError: property 'language' of 'KeyBoard' object has no setter
	print(kb.language)
