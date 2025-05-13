import csv
from datetime import datetime

class Validate:
	def __init__(self, file):
		self.filename		=	file
		self.raw_sells		=	[]
		self.clear_sells	=	[]

	def load_data(self):
		with open(self.filename,'r', encoding='utf-8') as file:
			reader = csv.DictReader(file)

			self.raw_sells = list(reader)

	@staticmethod
	def check_diap(name, price, amount, args):
		#? Слишком длинное наименование
		if len(name) > args.max_name or len(name) < args.min_name:
			return False
		#? Цена не принадлежит к допустимому диапазону
		if price > args.max_price or price < args.min_price:
			return False
		#? Количество не соответствует допустимому диапазону
		if amount > args.max_amount or amount < args.min_amount:
			return False
		return True

	def fix_raw_data(self, args):
		for i in range (0, len(self.raw_sells)):
			name	=	str(self.raw_sells[i]['name'])
			price	=	int(self.raw_sells[i]['price'])
			amount	=	int(self.raw_sells[i]['amount'])

			a = {}

			if not self.check_diap(name, price, amount, args) or a in self.clear_sells:
				continue
			else:
				a['name']		=	name
				a['price']		=	price
				a['amount']		=	amount
				a['sell_date']	=	datetime.strptime(self.raw_sells[i]['sell_date'], '%Y-%m-%d %H:%M:%S')

				self.clear_sells.append(a)