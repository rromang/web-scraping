from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
from scrape_mars import *

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#example from: https://www.geeksforgeeks.org/mongodb-python-insert-update-data/
try:
    conn = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(conn)
    print('Connected successfully!')
except:
    print('Could not connect to MongoDB')

db = client['marsDB']
print("Database created........")

print("List of databases after creating new one")
print(client.list_database_names())

MarsInfo = db.MarsInfo

# print(db.list_collection_names())

data = [scrape()]

print(data)
print(type(data))

data_dict = {}
for x in data:
    data_dict.update(x)
print(data_dict)


# MarsInfo.insert_one(data_dict)


#print list of the _id values of the inserted documents:

db.MarsInfo.insert_one(data_dict)

# cursor = db.MarsInfo.find()
# for record in cursor:
#     print(record)
  
# Printing the data inserted
# Route to render index.html template using data from Mongo
# @app.route("/")
# def home():



# # Route that will trigger the scrape function
# @app.route("/scrape")
 

# if __name__ == "__main__":
#     app.run(debug=True)
