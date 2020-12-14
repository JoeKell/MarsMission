from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define database and collection
db = client.Mars_App_db
collection = db.items


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    items=db.items.find()
    for item in items:
        print(item)
        print()
        print(item['Headline'])
    # Return template and data
    return "<h1>Thanks for visiting the page</h1>" 
    # return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def app_scrape():

    #Drop the existing data and scrape new data
    collection.drop()
    collection.insert_one(scrape())

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


