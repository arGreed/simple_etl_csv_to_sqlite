#from sells_gen import Sells_gen
from validate import Validate
import argparse
#a = Sells_gen('name.csv')
#a.gen_fake_shop_report()


def get_parser():
	parser = argparse.ArgumentParser(description='Перечень диапазонов допустимых значений для работы приложения')

	parser.add_argument('--min_name_len', type = int, required = True, dest = 'min_name', help = 'Минимально допустимая длина наименования товара')
	parser.add_argument('--max_name_len', type = int, required = True, dest = 'max_name', help = 'Максимальная допустимая длина наименования товара')
	parser.add_argument('--min_price', type = int, required = True, dest = 'min_price', help = 'Минимальная допустимая цена товара')
	parser.add_argument('--max_price', type = int, required = True, dest = 'max_price', help = 'Максимальная допустимая цена товара')
	parser.add_argument('--min_amount', type = int, required = True, dest = 'min_amount', help = 'Минимально допустимое количество товара при покупке')
	parser.add_argument('--max_amount', type = int, required = True, dest = 'max_amount', help = 'Максимально допустимое количество товара при покупке')

	return parser

def main():
	parser = get_parser()
	args = parser.parse_args()

	a = Validate('name.csv')

	a.load_data()
	a.fix_types(args)


if __name__ == '__main__':
	main()
