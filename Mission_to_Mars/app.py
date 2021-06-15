from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
# import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#example from: https://www.geeksforgeeks.org/mongodb-python-insert-update-data/
try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print('Connected successfully!')
except:
    print('Could not connect to MongoDB')


# database
mars_db = myclient.database
  
# Created or Switched to collection names: my_gfg_collection
collection = mars_db.my_gfg_collection
  
emp_rec1 = {
        "name":"Mr.Geek",
        "eid":24,
        "location":"delhi"
        }
emp_rec2 = {
        "name":"Mr.Shaurya",
        "eid":14,
        "location":"delhi"
        }
  
# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)
  
print("Data inserted with record ids",rec_id1," ",rec_id2)
  
# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)

# Route to render index.html template using data from Mongo
# @app.route("/")
# def home():



# # Route that will trigger the scrape function
# @app.route("/scrape")
 

# if __name__ == "__main__":
#     app.run(debug=True)
