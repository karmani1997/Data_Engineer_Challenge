from typing import List

import mongoengine as me

from .models import CakeModel
from .models import CakeMongoOrm

def connect():
	"""
	Connects to the database
	"""
	me.connect("cakes")


class Loader:
	def __init__(self, cake_data: List[CakeModel]):
		"""
		This class loads transformed data into the database

		Args:
		    cake_data: transformed data
		"""
		connect()
		self.cake_data = cake_data

	def load_data(self):
		"""
		Inserts data into the database
		"""

		for cake in self.cake_data:
			try:

				CakeMongoOrm(entry_id = cake.entry_id, name = cake.name, diameter_in_mm = cake.diameter_in_mm, vegan = cake.vegan, original_unit = cake.original_unit).save()
			except:
				#print("Error while inserting data")
				return False
		#print ("Data Loaded Successfully")
		return True
