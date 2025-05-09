
from random import choice
from random import randint
from datetime import datetime

import csv

class Sells_gen:

	def __init__(self, file_name):
		self.file_name = file_name

	@staticmethod
	def prep_goods():
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
	def gen_fake_data():
		date = datetime.strptime(f'2025-05-{randint(1,31)} {randint(1,23)}:{randint(1,59)}:{randint(1,59)}', '%Y-%m-%d %H:%M:%S')

		return date

	def gen_fake_shop_report(self):
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
