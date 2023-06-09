import pytest

from src.keyboard import *


@pytest.fixture
def kb() -> Keyboard:
	return Keyboard('Dark Project KD87A', 9600, 5)


def test_srt(kb):
	assert str(kb.language) == "EN"


def test_change_lang(kb):
	kb.change_lang()
	assert str(kb.language) == "RU"


def test_change_lang_change_lang(kb):
	kb.change_lang().change_lang()
	assert str(kb.language) == "EN"


def test_language_setter(kb):
	with pytest.raises(AttributeError):
		kb.language = 'CH'
