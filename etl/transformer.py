from typing import List, Optional
from itertools import groupby

from .models import CakeModel
from .models import VALID_CAKE_FLAVORS


class Transformer:
	def __init__(self, raw_data: List[dict]):
		"""
		This class transforms extracted data according to the desired model

		Args:
		    raw_data: extracted data
		"""
		self.raw_data = raw_data

	def transform_data(self) -> List[CakeModel]:
		"""
		Transforms data

		Returns:
		    transformed data as a list of models
		"""
		transformed_cakes = list()
		for in_cake in self.raw_data:
			out_cake = self.transform_single_item(in_cake)
			if out_cake:
				transformed_cakes.append(out_cake)
		return transformed_cakes

	def transform_single_item(self, input_item: dict) -> Optional[CakeModel]:
		"""
		Transforms single item of extracted data

		Args:
		    input_item: part of extracted data

		Returns:
		    model if transformation was successful
		"""
		# Extract values from dict through keys, convert the string value into lower cases and remove the space and inverted comma
		entry = input_item['entry']
		diameter = input_item['cake_diameter'].lower()
		unit = input_item['diam_unit'].lower().strip().replace("\"",'')
		flavor = input_item['flavor'].lower().strip().replace("\"",'')
		is_cake_vegan = input_item['is_cake_vegan'].lower().strip().replace("\"",'')
		
		# Parse the diameter value to separate the value and unit
		try:
			res = [''.join(g).strip() for _, g in groupby(diameter.replace("\"",''), str.isalpha)]
			diameter = float(res[0].replace(" ",''))
			d_unit = res[1].replace(" ",'')
		except ValueError:
			return None
		except IndexError:
			d_unit = unit
			
		#assign "in" if the unit is inch
		if d_unit == 'in' or d_unit == 'inches' or d_unit == 'inch': 
			d_unit = 'in'
		#assign "m" if unit is meter
		if d_unit == 'm' or d_unit == 'meters' or d_unit == 'meter':
			d_unit = 'm'
			
		#assign "m" if unit is meter
		if unit == 'm' or unit == 'meters' or unit == 'meter':
    			unit = 'm'

		#assign "in" if unit is inch
		if unit == 'in' or unit == 'inches' or unit == 'inch':
			unit = 'in'
		#assign default unit mm
		if unit != "in" and unit != "m" and d_unit != "in" and d_unit != "m":
			unit = "mm"
			d_unit = "mm"
		# if the unit is not attached wih in column assign diameter string unit
		if d_unit == "":
			d_unit = unit
		# if the unit is not attached with diameter assign unit
		if unit == "":
			unit = d_unit
	
    		#return if the unit is mismatch
		if unit != d_unit:
			return None					
			
			
		#if the diameter value in the inches convert it into mm
		if d_unit == 'in' and unit == 'in': 
			diameter = diameter*25.4
			unit = 'in'
		#if the diameter value in the meters convert it into mm
		elif d_unit == 'm' and unit == 'm':
			diameter = diameter*1000
			unit = 'm'
		# Otherwise assign mm unit by default
		else:
			unit = 'mm'
			
		#if cake is not vegan then assign False value
		if is_cake_vegan == 'false' or is_cake_vegan == 'no' or is_cake_vegan == '0' or is_cake_vegan == 'f':
			is_cake_vegan = False
		#if cake is vegan then assign True value
		elif is_cake_vegan == 'true' or is_cake_vegan == 'yes' or is_cake_vegan == '1' or is_cake_vegan == 't':
			is_cake_vegan = True
		#Oherwise assign None
		else:
			is_cake_vegan = None
			
		#Validate the falovour value
		if flavor not in set(VALID_CAKE_FLAVORS):
			flavor = None
		# To store the CakeModel Object
		cake = None
		try:
			#Create CakeModel Object to validate the extracted values	
			cake = CakeModel(entry_id = entry, diameter_in_mm = diameter, name = flavor, vegan = is_cake_vegan, original_unit = unit)
		except:
			print ("Error in data parsing")
			return None
		#Return the CakeModel Object
		return cake        
		
		
		
		
