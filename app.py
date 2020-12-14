from scrape_mars import scrape
import pymongo

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define database and collection
db = client.Mars_App_db
collection = db.items
collection.drop()
collection.insert_one(scrape())