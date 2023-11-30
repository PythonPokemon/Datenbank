# 1 import installieren
import pymongo

# 2 mongo db account erstellen + anbinden
conn_str = "mongodb+srv://PythonPokemon:PythonPokemon2023@cluster0.11e0iuw.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error:" + Exception)


# 3 DB erstellen
myDB = client["pymongo_demo"]

# 4 Kollection erstellen
myCollction = myDB["demo_collection"]

# 5  document aufzeichnen
myDoc = {
    "_id": 1,
    "name":"PythonPokemon",
    "message": "das ist eine pymongo demo"
}

# dokument inserieren
res = myCollction.insert_one(myDoc)

print(res.inserted_id)
print(client.list_database_names())