"""Run this script to launch the pipeline"""

from etl.master import run_etl
from subprocess import call

if __name__ == "__main__":
	run_etl("cake_data.csv")

	call(["python3", "Report/app.py"])	
