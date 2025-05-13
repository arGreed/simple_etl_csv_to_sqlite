from validate import Validate
from db_operations import DB_operations
from aggregate import Aggregate

import argparse


def get_parser():
	parser = argparse.ArgumentParser(description='Перечень диапазонов допустимых значений для работы приложения')

	parser.add_argument('--min_name_len',	type = int,	required = True,	dest = 'min_name',		help = 'Минимально допустимая длина наименования товара')
	parser.add_argument('--max_name_len',	type = int,	required = True,	dest = 'max_name',		help = 'Максимальная допустимая длина наименования товара')
	parser.add_argument('--min_price',		type = int,	required = True,	dest = 'min_price',		help = 'Минимальная допустимая цена товара')
	parser.add_argument('--max_amount',		type = int,	required = True,	dest = 'max_amount',	help = 'Максимально допустимое количество товара при покупке')
	parser.add_argument('--max_price',		type = int,	required = True,	dest = 'max_price',		help = 'Максимальная допустимая цена товара')
	parser.add_argument('--min_amount',		type = int,	required = True,	dest = 'min_amount',	help = 'Минимально допустимое количество товара при покупке')

	return parser

def main():
	parser = get_parser()
	args = parser.parse_args()

	a = Validate('name.csv')

	a.load_data()
	a.fix_raw_data(args)

	b = Aggregate()
	b.set_clear_data(a.clear_sells)
	b.calc_params()

	c = DB_operations()
	c.set_db_name('test.db')
	c.auto_migrate()

	c.insert_raw_data(b.clear_data)
	c.insert_aggregated_data(b.good_aggregated_data)

if __name__ == '__main__':
	main()
