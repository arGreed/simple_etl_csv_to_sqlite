import csv
import logging

from datetime import datetime

class Validate:
	def __init__(self, file: str):
		"""
		Инициализирует экземпляр класса Validate.

		Загружает данные из указанного файла.
		Подготавливает списки для хранения "сырых" и "очищенных" данных.

		Args:
			file (str): Путь к указанному CSV-файлу
		Attributes:
			filename (str): наименование файла, содержащего необработанные данные
			raw_sells (list): Список "сырых" записей из файла
			clear_sells (list): Список отфильтрованных и корректных записей
		"""
		self.logger = logging.getLogger(__name__)
		self.filename		=	file
		self.raw_sells		=	[]
		self.clear_sells	=	[]

	def load_data(self):
		"""
		Загрузка данных из указанного CSV-файла в память программы

		Метод открывает файл, указанный при инициализации объекта и считывает
		содержимое посредством DictReader. Результат сохраняется в атрибут
		raw_sells в виде списка словарей
		"""
		with open(self.filename,'r', encoding = 'utf-8') as file:
			reader = csv.DictReader(file)

			self.raw_sells = list(reader)

	@staticmethod
	def check_diap(name: str, price: int, amount: int, args) -> bool:
		"""
		Проверка корректности данных

		Метод получает на вход параметры из необработанной строки, полученной из
		CSV-файла и аргументы, введённые при запуске приложения. Далее происходит
		проверка принадлежности значений к полученным диапазонам.
		
		Returns:
			bool:
				False - какой-либо из параметров не принадлежит к допустимым диапазонам
				True - если все параметры соответствуют допустимым диапазонам
		Args:
			name (str): наименование продукта
			price (int): цена продукта
			amount (int): количество товаров
			args: Объект с атрибутами:
				- min_name (int): Минимальная длина названия
				- max_name (int): Максимальная длина названия
				- min_price (int): Минимальная цена
				- max_price (int): Максимальная цена
				- min_amount (int): Минимальное количество
				- max_amount (int): Максимальное количество
		"""
		#? Слишком длинное наименование
		if not(args.max_name >= len(name) >= args.min_name):
			return False
		#? Цена не принадлежит к допустимому диапазону
		if not(args.max_price >= price >= args.min_price):
			return False
		#? Количество не соответствует допустимому диапазону
		if not(args.max_amount >= amount >= args.min_amount):
			return False
		return True

	def fix_raw_data(self, args):
		"""
		Валидация данных

		Метод, проверяющий типы полученных данных, их принадлежность
		к допустимым диапазонам и формирующий перечень очищенных значений

		args: Объект с атрибутами:
				- min_name (int): Минимальная длина названия
				- max_name (int): Максимальная длина названия
				- min_price (int): Минимальная цена
				- max_price (int): Максимальная цена
				- min_amount (int): Минимальное количество
				- max_amount (int): Максимальное количество
		"""
		for i in range (0, len(self.raw_sells)):
			name	=	str(self.raw_sells[i]['name'])
			price	=	int(self.raw_sells[i]['price'])
			amount	=	int(self.raw_sells[i]['amount'])

			a = {}

			if not self.check_diap(name, price, amount, args):
				continue
			else:
				a['name']		=	name
				a['price']		=	price
				a['amount']		=	amount
				a['sell_date']	=	datetime.strptime(self.raw_sells[i]['sell_date'], '%Y-%m-%d %H:%M:%S')
				if a not in self.clear_sells:
					self.clear_sells.append(a)