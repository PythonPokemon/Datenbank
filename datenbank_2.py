import mysql.connector

def verbinde_zur_datenbank():
    try:
        meine_datenbank = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="tourplaner"
        )
        return meine_datenbank
    except mysql.connector.Error as err:
        print(f"Fehler bei der Verbindung zur Datenbank: {err}")
        return None

def daten_einfuegen(meine_datenbank, datum, ort, ort_name):
    sql = "INSERT INTO Konzerte (Datum, Ort, Ort_Name) VALUES (%s, %s, %s)"
    daten = (datum, ort, ort_name)

    try:
        with meine_datenbank.cursor() as mein_greifarm:
            mein_greifarm.execute(sql, daten)
        meine_datenbank.commit()
        print("Daten erfolgreich eingefügt.")
    except mysql.connector.Error as err:
        print(f"Fehler beim Einfügen der Daten: {err}")

def alle_daten_anzeigen(meine_datenbank):
    sql = "SELECT * FROM Konzerte"
    with meine_datenbank.cursor() as mein_greifarm:
        mein_greifarm.execute(sql)
        result = mein_greifarm.fetchall()

    for row in result:
        print(row)

def alle_datenbanken_anzeigen(meine_datenbank):
    with meine_datenbank.cursor() as mein_greifarm:
        mein_greifarm.execute("SHOW DATABASES")
        databases = mein_greifarm.fetchall()
        for db in databases:
            print(db[0])

if __name__ == "__main__":
    meine_datenbank = verbinde_zur_datenbank()
    if meine_datenbank:
        daten_einfuegen(meine_datenbank, '2020-10-10', 'Freiburg', 'Weingarten')
        alle_daten_anzeigen(meine_datenbank)
        alle_datenbanken_anzeigen(meine_datenbank)
        meine_datenbank.close()
