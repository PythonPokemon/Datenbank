import pymongo

# Verbindung zur MongoDB-Datenbank herstellen
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Hier die Verbindungs-URL entsprechend Ihrer MongoDB-Konfiguration anpassen

# Datenbank und Sammlung auswählen
db = client["IhreDatenbankName"]  # Hier den Namen Ihrer Datenbank angeben
collection = db["Monitore"]

# Einfügen eines Datensatzes
monitor_data = {
    "MonitorID": 1,
    "Name": "UW3420K",
    "Preis": 343.50,
    "Größe": "34 Zoll"
}

collection.insert_one(monitor_data)

# Abfrage aller Datensätze in der Sammlung und Ausgabe in der Konsole
cursor = collection.find()
for document in cursor:
    print(document)

# Verbindung schließen
client.close()
