
from flask_pymongo import pymongo
from scrape_mars import *

# Create an instance of Flask
# app = Flask(__name__)
  

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

# title_news = MarsInfo.find_one()
# print(title_news)

print(db.list_collection_names())

data = scrape()
print([item for item in data])

MarsInfo.insert_many([item for item in data])
cursor = MarsInfo.find()
for record in cursor:
    print(record)



  
# Printing the data inserted
# Route to render index.html template using data from Mongo
# @app.route("/")
# def home():

#     # Find one record of data from the mongo database
#     mars_info = db.MarsInfo.find_one()
    
#     # Return template and data
#     return render_template("index.html", mars_data=mars_info)


# # # # Route that will trigger the scrape function
# # @app.route("/scrape")
# # def scrape():

# #     mars_data = scrape.scrape_info()

# #     # MarsInfo.insert_many(data)
# #     MarsInfo.update({}, mars_data, upsert=True)


# #     # Redirect back to home page
# #     return redirect("/")


# if __name__ == "__main__":
#     app.run(debug=True)
