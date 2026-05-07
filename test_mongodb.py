from pymongo import MongoClient

uri = "mongodb+srv://23375072_db_user:Sudipta%40123@cluster0.wxwmekw.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)