# Importiere das mysql.connector-Modul, das für die Verbindung zur MySQL-Datenbank verwendet wird.
import mysql.connector

# Funktion zur Verbindung zur Datenbank
def verbinde_zur_datenbank():
    try:
        # Verbinde zur MySQL-Datenbank mit den angegebenen Parametern
        meine_datenbank = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="tourplaner"
        )
        return meine_datenbank
    except mysql.connector.Error as err:
        # Bei einem Fehler während der Verbindung zur Datenbank, gibt eine Fehlermeldung aus
        print(f"Fehler bei der Verbindung zur Datenbank: {err}")
        return None

# Funktion zum Einfügen von Daten in die Konzerte-Tabelle
def daten_einfuegen(meine_datenbank, datum, ort, ort_name):
    # SQL-Anweisung mit Platzhaltern für Datum, Ort und Ort_Name
    sql = "INSERT INTO Konzerte (Datum, Ort, Ort_Name) VALUES (%s, %s, %s)"
    daten = (datum, ort, ort_name)

    try:
        # Verwende einen "with"-Block, um sicherzustellen, dass die Ressourcen ordnungsgemäß freigegeben werden
        with meine_datenbank.cursor() as mein_greifarm:
            # Führe die SQL-Anweisung mit den Daten aus
            mein_greifarm.execute(sql, daten)
        # Commit, um die Änderungen in der Datenbank zu speichern
        meine_datenbank.commit()
        print("Daten erfolgreich eingefügt.")
    except mysql.connector.Error as err:
        # Bei einem Fehler während des Einfügens, gibt eine Fehlermeldung aus
        print(f"Fehler beim Einfügen der Daten: {err}")

# Funktion zur Anzeige aller Daten in der Konzerte-Tabelle
def alle_daten_anzeigen(meine_datenbank):
    # SQL-Anweisung zum Abrufen aller Datensätze aus der Konzerte-Tabelle
    sql = "SELECT * FROM Konzerte"
    with meine_datenbank.cursor() as mein_greifarm:
        # Führe die SQL-Anweisung aus und hole die Ergebnisse
        mein_greifarm.execute(sql)
        result = mein_greifarm.fetchall()

    # Gehe durch die Ergebnisse und gebe sie aus
    for row in result:
        print(row)

# Funktion zur Anzeige aller Datenbanken auf dem Server
def alle_datenbanken_anzeigen(meine_datenbank):
    with meine_datenbank.cursor() as mein_greifarm:
        # SQL-Anweisung zum Anzeigen aller Datenbanken auf dem Server
        mein_greifarm.execute("SHOW DATABASES")
        databases = mein_greifarm.fetchall()
        for db in databases:
            # Gebe den Namen der Datenbank aus (Index 0 enthält den Namen)
            print(db[0])

# Hauptprogramm: Überprüfe, ob dieses Skript direkt ausgeführt wird
if __name__ == "__main__":
    # Verbinde zur Datenbank
    meine_datenbank = verbinde_zur_datenbank()
    
    if meine_datenbank:
        # Führe verschiedene Operationen aus, einschließlich Einfügen von Daten und Anzeigen von Informationen
        daten_einfuegen(meine_datenbank, '2020-10-10', 'Freiburg', 'Weingarten')
        alle_daten_anzeigen(meine_datenbank)
        alle_datenbanken_anzeigen(meine_datenbank)
        
        # Schließe die Verbindung zur Datenbank am Ende des Programms
        meine_datenbank.close()
