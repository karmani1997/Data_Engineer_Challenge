from etl.extractor import Extractor
from unittest.case import TestCase
import pandas as pd

class TestExtractor(TestCase):
    
    
	def test_extractor_valid_file(self):
		extractor = Extractor(in_file_path="cake_data.csv")
		res = extractor.extract_data()
		self.assertEqual(type(res), type([{1:2}]))
		print ("test_extractor_valid_file testcase run successfully")

	def test_extractor_invalid_file(self):
		extractor = Extractor(in_file_path="cake_data1.csv")
		res = extractor.extract_data()
		self.assertEqual(res, [{}])
		print ("test_extractor_invalid_file testcase run successfully")
		        
if __name__ == '__main__':
	unittest.main()   

