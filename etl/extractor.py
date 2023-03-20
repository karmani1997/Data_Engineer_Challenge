from typing import List
import pandas as pd

class Extractor:
	def __init__(self, in_file_path: str):
		"""
		This class extracts data from source file

		Args:
		    in_file_path: path to the source file
		"""
		self.in_file_path = in_file_path

	def extract_data(self) -> List[dict]:
		"""
		Extracts data from CSV file

		Returns:
		data as a list of dictionaries
		"""
		try:
			#Load the data from csv file
			df = pd.read_csv(self.in_file_path, delimiter='|', index_col=False)
			if df.shape[0] > 0:
				#convert the columns files
				df['cake_diameter'] = df['cake_diameter'].astype(str)
				df['diam_unit'] = df['diam_unit'].astype(str)
				df['flavor'] = df['flavor'].astype(str)
				df['is_cake_vegan'] = df['is_cake_vegan'].astype(str)

				#Return the record as list of dicts
				return df.to_dict('records')
			else:
				return [{}]
		except:
			return [{}]
