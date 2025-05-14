
from random import choice
from random import randint
from datetime import datetime

import logging
import csv

class Sells_gen:

	def __init__(self, file_name: str):
		"""
		Инициализирует экземпляр класса Sells_gen

		Генерирует случайные данные по продажам и записывает их в CSV-файл

		Args:
			file_name (str): Наименование файла, в который будут записаны сгенерированные значения
		"""
		self.logger = logging.getLogger(__name__)
		self.file_name = file_name

	@staticmethod
	def prep_goods() -> dict:
		"""
		Геттер перечня товаров

		Return:
			Словарь товаров с их ценами
		"""
		goods_n_prices = {
			'Milk': 12,
			'Soap': 19,
			'Cherry':24,
			'Potato':3,
			'Chips':44,
			'Soda':10
		}
		return goods_n_prices
	
	@staticmethod
	def gen_fake_data() -> datetime:
		"""
		Формирование случайной даты

		Метод генерирует случайную дату в диапазоне 2025-05-01 01:01:01 - 2025-05-31 59:59:59
		"""
		date = datetime.strptime(f'2025-05-{randint(1,31)} {randint(1,23)}:{randint(1,59)}:{randint(1,59)}', '%Y-%m-%d %H:%M:%S')

		return date

	def gen_fake_shop_report(self):
		"""
		Запись сгенерированных значений в CSV-файл

		Метод генерирует случайную историю продаж перечня продуктов, записывает полученные данные в лист словарей
		и записывает сгенерированные значения в CSV-файл
		"""
		goods = self.prep_goods()
		rez = []
		for _ in range (1000):
			rand_good = choice(list(goods.items()))
			size = randint(1,15)
			sell = {
				'name':rand_good[0],
				'price':rand_good[1],
				'amount':size,
				'sell_date':self.gen_fake_data()
			}
			rez.append(sell)
		keys = rez[0].keys()
		with open(self.file_name, 'w', encoding='utf-8') as file:
			writer = csv.DictWriter(file, fieldnames=keys, lineterminator='\n')

			writer.writeheader()
			writer.writerows(rez)
