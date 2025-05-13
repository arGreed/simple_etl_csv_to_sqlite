class Aggregate:
	def __init__(self):
		self.clear_data = []
		self.good_aggregated_data = {}

	def set_clear_data(self, clear_data):
		self.clear_data = clear_data

	@staticmethod
	def calc_avg(clear_data, rez):
		for i in rez.keys():
			orders_cnt = sum(1 for item in clear_data if item['name'] == i)
			rez[i]['avg_order'] = rez[i]['total_money'] / orders_cnt

	@staticmethod
	def calc_total_money(clear_data, rez):
		for i in rez.keys():
			product_itog = sum(item['amount'] * item['price'] for item in clear_data if item['name'] == i)
			rez[i]['total_money'] = product_itog

	@staticmethod
	def calc_total_amount(clear_data, rez):
		for i in rez.keys():
			product_itog = sum(item['amount'] for item in clear_data if item['name'] == i)
			rez[i]['total_amount'] = product_itog


	@staticmethod
	def get_keys(clear_data):
		return {item['name'] for item in clear_data}

	def calc_params(self):
		keys = self.get_keys(self.clear_data)
		rez = {}
		for i in keys:
			rez[i] = {
				'total_money':0,
				'total_amount':0,
				'avg_order':0
			}
		self.calc_total_amount(self.clear_data, rez)
		self.calc_total_money(self.clear_data, rez)
		self.calc_avg(self.clear_data, rez)

		self.good_aggregated_data = rez