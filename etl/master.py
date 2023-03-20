from .extractor import Extractor
from .loader import Loader
from .transformer import Transformer


def run_etl(input_file: str):
	"""
	Runs whole ETL pipeline

	Args:
	input_file: path to the source file
	"""
	extractor = Extractor(input_file)
	transformer = Transformer(extractor.extract_data())
	loader = Loader(transformer.transform_data())

	loader.load_data()
