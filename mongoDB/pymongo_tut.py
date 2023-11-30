#step 1 install import
import pymongo

#step 2 create a mongo db client
conn_str = "mongodb+srv://PythonPokemon:PythonPokemon2023@cluster0.11e0iuw.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error:" + Exception)

#create
#step 3 create a DB
myDB = client["pymongo_demo"]

# step 4 - create a collection
myCollction = myDB["demo_collection"]

# step 5 Create a document/record
myDoc = {
    "_id": 1,
    "name":"PythonPokemon",
    "message": "das ist eine pymongo demo"
}

# insert the document
res = myCollction.insert_one(myDoc)

print(res.inserted_id)
print(client.list_database_names())