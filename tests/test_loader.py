from etl.loader import Loader
from unittest.case import TestCase
from etl.models import CakeModel

class TestLoader(TestCase):
    
    
    def test_loader_valid_data(self):
        loader = Loader(
            cake_data=[
                CakeModel(entry_id = 123334, diameter_in_mm = 56.78, name = 'caramel', vegan = False, original_unit = 'mm')
            ]
        )
        res = loader.load_data()
        self.assertEqual(res, True)
        print ("test_loader_valid_data testcase run successfully")

    def test_loader_duplicate_key(self):
        loader = Loader(
            cake_data=[
                CakeModel(entry_id = 239, diameter_in_mm = 56.78, name = 'caramel', vegan = False, original_unit = 'mm')
            ]
        )
        res = loader.load_data()
        self.assertEqual(res, False)
        print ("test_loader_duplicate_key testcase run successfully")

    def test_loader_valid_type_data(self):
        loader = Loader(
            cake_data=[
                CakeModel(entry_id = "239123", diameter_in_mm = 56.78, name = 'caramel', vegan = False, original_unit = 'm')
            ]
        )
        res = loader.load_data()
        self.assertEqual(res, True)
        print ("test_loader_valid_type_data testcase run successfully")

    def test_loader_valid_type_data_diameter(self):
        loader = Loader(
            cake_data=[
                CakeModel(entry_id = 239123, diameter_in_mm = "56.78", name = 'caramel', vegan = False, original_unit = 'in')
            ]
        )
        res = loader.load_data()
        self.assertEqual(res, False)
        print ("test_loader_valid_type_data_diameter testcase run successfully")


if __name__ == '__main__':
    unittest.main()   
    
