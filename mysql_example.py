# importiere sql aus der python Bibliothek
import mysql.connector

# erstelle datenbank
meine_datenbank = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123",
    database = "tourplaner"
)

# meine datenbank ausgeben
print(meine_datenbank)

# auf die datenbank zugreifen
mein_greifarm = meine_datenbank.cursor()

# befehl um etwas in der datenbank auszufüheren 'execute'
mein_greifarm.execute("CREATE DATABASE tourenplaner")
mein_greifarm.execute("SHOW DATABASES")

# zeigt alle datenbanken auf, die gefunden werden.
for db in mein_greifarm:
    print(db)