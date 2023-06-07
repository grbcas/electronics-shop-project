"""Тесты с использованием pytest для модуля Phone."""
import pytest
from src.item import *
from src.phone import *

PATH_CSV = Path(Path(__file__), 'data', 'items.csv')


@pytest.fixture
def data() -> Phone:
	return Phone("iPhone 14", 120_000, 5, 2)


def test_validate_number_of_sim():
	with pytest.raises(ValueError):
		Phone("iPhone 14", 120_000, 5, 0)


def test_repr(data):
	assert repr(data) == "Phone('iPhone 14', 120000, 5, 2)"


def test_srt(data):
	assert str(data) == 'iPhone 14'
