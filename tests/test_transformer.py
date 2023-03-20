from etl.transformer import Transformer
from unittest.case import TestCase


class TestTransformer(TestCase):
    
    
    def test_transformer_valid_unit_mm(self):
        transformer = Transformer(
        raw_data=[
                {
                    "entry": "1",
                    "cake_diameter": "56.78mm",
                    "diam_unit": "mm",
                    "flavor": "caramel",
                    "is_cake_vegan": "1",
                },
                            {
                    "entry": "1",
                    "cake_diameter": "56.78",
                    "diam_unit": "mm",
                    "flavor": "caramel",
                    "is_cake_vegan": "True",
                },
                                {
                    "entry": "1",
                    "cake_diameter": "56.78mm",
                    "diam_unit": "",
                    "flavor": "caramel",
                    "is_cake_vegan": "t",
                }
        ])
        for i in range(3):
            res = transformer.transform_data()[i]
            self.assertEqual(res.entry_id, 1)
            self.assertEqual(res.name, "caramel")
            self.assertEqual(res.diameter_in_mm, 56.78)
            self.assertTrue(res.vegan)
            self.assertEqual(res.original_unit, "mm")
            print ("test_transformer_valid_unit_mm TestCase Run Successfully")
        
    def test_transformer_valid_unit_in(self):
        transformer = Transformer(
        raw_data=[
                {
                    "entry": "1",
                    "cake_diameter": "56.78in",
                    "diam_unit": "in",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                },
                 {
                    "entry": "1",
                    "cake_diameter": "56.78in",
                    "diam_unit": "",
                    "flavor": "caramel",
                    "is_cake_vegan": "0",
                },
                            {
                    "entry": "1",
                    "cake_diameter": "56.78inches",
                    "diam_unit": "",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                },
                
        ])
        for i in range(3):
            res = transformer.transform_data()[i]
            self.assertEqual(res.entry_id, 1)
            self.assertEqual(res.name, "caramel")
            self.assertEqual(res.diameter_in_mm, 1442.212)
            self.assertFalse(res.vegan)
            self.assertEqual(res.original_unit, "in")
            print ("test_transformer_valid_unit_in TestCase Run Successfully")

    def test_transformer_valid_unit_m(self):
        transformer = Transformer(
        raw_data=[
                {
                    "entry": "1",
                    "cake_diameter": "56.78",
                    "diam_unit": "m",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                },
                
                                {
                    "entry": "1",
                    "cake_diameter": "56.78m",
                    "diam_unit": "m",
                    "flavor": "caramel",
                    "is_cake_vegan": "0",
                },
                
                                {
                    "entry": "1",
                    "cake_diameter": "56.78m",
                    "diam_unit": "",
                    "flavor": "caramel",
                    "is_cake_vegan": "f",
                },
                
        ])
        for i in range(3):
        	res = transformer.transform_data()[0]
        	self.assertEqual(res.entry_id, 1)
        	self.assertEqual(res.name, "caramel")
        	self.assertEqual(res.diameter_in_mm, 56780)
        	self.assertFalse(res.vegan)
        	self.assertEqual(res.original_unit, "m")
        	print ("test_transformer_valid_unit_m TestCase Run Successfully")

    def test_transformer_default_unit_mm_is_vegan(self):
        transformer = Transformer(
        raw_data=[
                {
                    "entry": "1",
                    "cake_diameter": "56.78",
                    "diam_unit": "",
                    "flavor": "caramel",
                    "is_cake_vegan": "1",
                }
                
        ])
        res = transformer.transform_data()[0]
        self.assertEqual(res.entry_id, 1)
        self.assertEqual(res.name, "caramel")
        self.assertEqual(res.diameter_in_mm, 56.78)
        self.assertTrue(res.vegan)
        self.assertEqual(res.original_unit, "mm")
        print ("test_transformer_default_unit_mm TestCase Run Successfully")
    
    def test_transformer_invalid_input(self):
        transformer = Transformer(
        raw_data=[
                {
                    "entry": "1",
                    "cake_diameter": "store",
                    "diam_unit": "",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                },
                            {
                    "entry": "1",
                    "cake_diameter": "123m",
                    "diam_unit": "in",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                },
                          {
                    "entry": "1",
                    "cake_diameter": "123in",
                    "diam_unit": "mm",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                },
                
        ])
        res = transformer.transform_data()
        self.assertEqual(len(res), 0)
        print ("test_transformer_invalid TestCase Run Successfully")
    
        
        
if __name__ == '__main__':
    unittest.main()  
