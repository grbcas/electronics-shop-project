"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *

path_csv_test = Path(Path(__file__).parent, 'data', 'test_items.csv')
path_csv_no_file = Path(Path(__file__).parent, 'data', '_items.csv')
path_csv_damaged_file = Path(Path(__file__).parent, 'data', 'test_items_damaged.csv')


@pytest.fixture
def data() -> Item:
	return Item("Смартфон", 10000, 20)


def test_calculate_total_price(data):
	"""
	тест функции расчёта общей цены товара в магазине
	"""
	assert data.calculate_total_price() == 200000


def test_apply_discount(data):
	"""
	тест функции расчёта скидки и нового уровня цены
	"""
	Item.pay_rate = 0.8
	data.apply_discount()
	assert data.price == 8000.0


def test_name_setter(data):
	data.name = 'test'
	assert data.name == 'test'


def test_repr(data):
	assert repr(data) == "Item('Смартфон', 10000, 20)"


def test_srt(data):
	assert str(data) == 'Смартфон'


def test_string_to_number():
	assert Item.string_to_number('5') == 5
	assert Item.string_to_number('5.0') == 5
	assert Item.string_to_number('5.5') == 5


def test_validate_name(data):
	with pytest.raises(ValueError):
		data.name = 'СуперСмартфон'


def test_instantiate_from_csv():
	Item.instantiate_from_csv(path_csv=path_csv_test)
	assert len(Item.all) == 5


def test_add():
	pass


def test_instantiate_from_csv_no_file():
	with pytest.raises(FileNotFoundError):
		Item.instantiate_from_csv(path_csv=path_csv_no_file)


def test_instantiate_from_damaged_file():
	with pytest.raises(InstantiateCSVError):
		Item.instantiate_from_csv(path_csv=path_csv_damaged_file)
