import sqlite3

class db_operations:
	def __init__(self):
		self.db_name	=	None
		self.conn		=	None
		self.cursor		=	None

	def set_db_name(self, db_name):
		self.db_name = db_name
	
	def prep_connect(self):
		self.conn = sqlite3.connect(self.db_name)
		self.cursor = self.conn.cursor()

	def close_connect(self):
		if self.conn:
			self.conn.close()

			self.conn = None
			self.cursor = None

	@staticmethod
	def get_raw_data_create():
		create_script = '''
			create table if not exists raw_data (
				id			integer primary key autoincrement,
				name		text,
				price		integer,
				amount		integer,
				sell_date	timestamp
			)
		'''

		return create_script
	

	@staticmethod
	def get_aggregated_data_create():
		create_script = '''
			create table if not exists aggregated_data (
				id				integer primary key autoincrement,
				name			text,
				total_money		integer,
				total_amount	integer,
				avg_order		real
			)
		'''

		return create_script
	
	@staticmethod
	def get_insert_raw_data():
		insert_script = '''
			insert into raw_data (
				name,
				price,
				amount,
				sell_date
			)
			values(
				?,
				?,
				?,
				?
			)
		'''

		return insert_script

	@staticmethod
	def get_insert_aggregated_data():
		insert_script = '''
			insert into aggregated_data (
				total_money,
				total_amount,
				avg_order,
				name
			)
			values(
				?,
				?,
				?,
				?
			)
		'''

		return insert_script

	def auto_migrate(self):
		self.prep_connect()

		self.cursor.execute(self.get_raw_data_create())
		self.cursor.execute(self.get_aggregated_data_create())

		self.conn.commit()

		self.close_connect()

	def insert_raw_data(self, raw_data):
		self.prep_connect()
		
		insert_script = self.get_insert_raw_data()

		for i in raw_data:
			pass
		
		self.conn.commit()
		self.close_connect()

	def insert_aggregated_data(self):
		self.prep_connect()

		insert_script = self.get_insert_aggregated_data()

		for i in raw_data:
			pass

		self.conn.commit()
		self.close_connect()