from src.item import *

class MixinLanguage:
	def change_lang(self):
		print(self.__dict__)
		if self.language == 'EN':
			self.__language = 'RU'
		else:
			self.__language = 'EN'
		print('MixinLanguage', self.__dict__)
		return self


class Keyboard(MixinLanguage, Item):
	def __init__(self, *args):
		super().__init__(*args)
		self.__language = 'EN'

	@property
	def language(self):
		return self.__language


# class Keyboard(MixinLanguage, Item):
# 	def __init__(self, *args):
# 		super().__init__(*args)
# 		self.__language = MixinLanguage.mixin_language

	# @property
	# def language(self):
	# 	print(self.__language)
	# 	return self.__language

# @language.setter
# def language(self, language):
# 	self.__language = language


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

	kb.language = 'CH'
	# # AttributeError: property 'language' of 'KeyBoard' object has no setter
	print(kb.language)
	print(kb.__dict__)
