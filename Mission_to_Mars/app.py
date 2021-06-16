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

data = scrape()

MarsInfo.insert_many(data)
# print(data)

# db.MarsInfo.insert_one(data.maps)

cursor = db.MarsInfo.find()
for record in cursor:
    print(record)

# print(type(data))


# data = [{'title_news': ["NASA's Ingenuity Mission Honored by the Space Foundation"], 'article_par': ['The mission picked up the 2021 John L. “Jack” Swigert, Jr., Award for Space Exploration for its history-making achievements.'], 'featured_image': 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html', 'mars_facts':              Parameters                         Values
# 0  Equatorial Diameter:                       6,792 km
# 1       Polar Diameter:                       6,752 km
# 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)
# 3                Moons:            2 (Phobos & Deimos)
# 4       Orbit Distance:       227,943,824 km (1.38 AU)
# 5         Orbit Period:           687 days (1.9 years)
# 6  Surface Temperature:                   -87 to -5 °C
# 7         First Record:              2nd millennium BC
# 8          Recorded By:           Egyptian astronomers, 'mars_images_full': [{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]}]

# data = [{'title_news': ["NASA's Ingenuity Mission Honored by the Space Foundation"], 'article_par': ['The mission picked up the 2021 John L. “Jack” Swigert, Jr., Award for Space Exploration for its history-making achievements.'], 'featured_image': 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'}]
# data_newstitle = {data[0]}

# data_dict = {}
# for x in data:
#     data_dict.update(x)
# print(data_dict)


# MarsInfo.insert_one(data_dict)


#print list of the _id values of the inserted documents:

# db.MarsInfo.insert_one(data_dict)

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
