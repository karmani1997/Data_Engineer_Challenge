from flask import Flask, request,render_template
from pymongo import MongoClient
import webbrowser

try:
	client = MongoClient("mongodb://localhost:27017") # connects to client locally
	db = client.cakes # get the database
except:
	print ("I am unable to connect to the database")
collection = db.cake_mongo_orm
app = Flask(__name__)
@app.route('/')
def index():
	
	rows = collection.find({"name":{"$ne" : None}, "vegan":{"$ne" : None}, })
	cakes_data = []
	for row in rows:
		cakes_data.append(row)
		
	rows = collection.find({"name": None, "vegan": None})
	cakes_data2 = []
	for row in rows:
		cakes_data2.append(row)


	return render_template('index.html', data = cakes_data,data2=cakes_data2)

@app.route('/vegan-data')
def form_example():
	rows = collection.find({"name": None, "vegan": None})
	cakes_data = []
	for row in rows:
		cakes_data.append(row)

	return render_template('index.html', data = cakes_data)



if __name__ == '__main__':
	webbrowser.open_new('http://127.0.0.1:2000/')
	app.run(host="0.0.0.0", port=2000)
    
    

