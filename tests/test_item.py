"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *


@pytest.fixture
def data():
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
