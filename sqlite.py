import sqlite3

# Funktion zur Verbindung zur SQLite-Datenbank
def verbinde_zur_datenbank():
    try:
        # Verbinde zur SQLite-Datenbank oder erstelle sie, wenn sie nicht existiert
        meine_datenbank = sqlite3.connect("tourplaner.db")
        return meine_datenbank
    except sqlite3.Error as err:
        # Bei einem Fehler während der Verbindung zur Datenbank, gibt eine Fehlermeldung aus
        print(f"Fehler bei der Verbindung zur Datenbank: {err}")
        return None

# Funktion zum Erstellen der Konzerte-Tabelle
def tabelle_erstellen(meine_datenbank):
    try:
        # SQL-Anweisung zur Erstellung der Konzerte-Tabelle
        mein_greifarm = meine_datenbank.cursor()
        mein_greifarm.execute('''CREATE TABLE IF NOT EXISTS Konzerte (
                                Datum TEXT,
                                Ort TEXT,
                                Ort_Name TEXT)''')
        meine_datenbank.commit()
        mein_greifarm.close()
    except sqlite3.Error as err:
        print(f"Fehler beim Erstellen der Tabelle: {err}")

# Funktion zum Einfügen von Daten in die Konzerte-Tabelle
def daten_einfuegen(meine_datenbank, datum, ort, ort_name):
    sql = "INSERT INTO Konzerte (Datum, Ort, Ort_Name) VALUES (?, ?, ?)"
    daten = (datum, ort, ort_name)

    try:
        mein_greifarm = meine_datenbank.cursor()
        mein_greifarm.execute(sql, daten)
        meine_datenbank.commit()
        mein_greifarm.close()
        print("Daten erfolgreich eingefügt.")
    except sqlite3.Error as err:
        print(f"Fehler beim Einfügen der Daten: {err}")

# Funktion zur Anzeige aller Daten in der Konzerte-Tabelle
def alle_daten_anzeigen(meine_datenbank):
    sql = "SELECT * FROM Konzerte"
    mein_greifarm = meine_datenbank.cursor()
    mein_greifarm.execute(sql)
    result = mein_greifarm.fetchall()

    for row in result:
        print(row)
    mein_greifarm.close()

# Hauptprogramm
if __name__ == "__main__":
    meine_datenbank = verbinde_zur_datenbank()
    
    if meine_datenbank:
        tabelle_erstellen(meine_datenbank)
        daten_einfuegen(meine_datenbank, '2020-10-10', 'Freiburg', 'Weingarten')
        alle_daten_anzeigen(meine_datenbank)

        meine_datenbank.close()
