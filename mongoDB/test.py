
from pymongo.mongo_client import MongoClient

uri = "mongodb://PythonPokemon:<PythonPokemon2023>@ac-4p88fi0-shard-00-00.11e0iuw.mongodb.net:27017,ac-4p88fi0-shard-00-01.11e0iuw.mongodb.net:27017,ac-4p88fi0-shard-00-02.11e0iuw.mongodb.net:27017/?ssl=true&replicaSet=atlas-w2r65g-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)