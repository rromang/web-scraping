from flask_pymongo import PyMongo
import flask
from flask import Flask, render_template, redirect
import scrape_mars

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/MarsDB")
db = mongodb_client.db


app.config["MONGO_URI"] = "mongodb://localhost:27017/MarsDB"
mongodb_client = PyMongo(app)
db = mongodb_client.db

mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsDB")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    information_data = mongo.db.collection.find_one({"title_news": True})

    # Return template and data
    return render_template("Mission_to_Mars/index.html", info=information_data)


@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
