# ETL Pipeline

## Description of the Project
In this task I have implemented the extractor, transformer and loader function separately, dump the data into the MongoDB and finally using to fetch the data from DB and show as Report on the webpage
* Extractor 
	> In this part I used Pandas dataframe to simply load the data and return as list of dictionaries to the transformer

* Transformer
	>In this function I parsed the data correctly and return as list of CakeModel object to the loader

* Loader
	>In this definition I used CakeMongoOrm object to insert the the MongoDB


## Run the Code and Test cases	

* Install requirement.txt file
* Install the requirements.txt using the following command 

	```
	pip3 install -r requirements.txt 
	```

### Run the MongoDB Docker Image
Instruction to run the local mongodb docker image 

* open terminal in the "challenge directory"
* run the following command to run mongodb image locally

	```
	docker run -ti --network=host mongo
	```
* Run the project to get clean data in a report
	```
		python3 main.py
	```
### Run the test cases

* To Test the Extractor Class run the following commmand in the terminal

	```
	python3 -m unittest tests.test_extractor
	```
* To Test the Transformer Class run the following command in the terminal

	``` python3 -m unittest tests.test_transformer
	```
* To Test the Loader Class run the following command in the terminal

	```
	python3 -m unittest tests.test_loader
	```

## Question Briefly answer: How could this ETL setup be improved? Are there any tools or frameworks that could be added?

* We can use aws cloud for this pipeline place the csv file in the S3 buckets and trigger the lambda function using glue job to dump the data in mongodb for the batch processing
* We can use Apache Spark there is a PySpark Frame in python to load the data, process it and dump it into the MongoDB for the batch processing



