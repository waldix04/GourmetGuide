#Noah import für die Datenbank (man muss davor noch MySQL downloaden auf https://dev.mysql.com/downloads/mysql/5.0.html, Konfiguration abschließen, dann ins VSC Terminal "pip3 install mysql-connector-python" )
import mysql.connector


#Noah Datenbank Variable
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8899",
    database="rezepte"
)
#cursor erledigt für uns die SQL-Befehle
my_cursor = my_db.cursor()

#beim ersten mal create database
#my_cursor.execute("CREATE DATABASE rezepte")
sql = """
        CREATE TABLE gerichte(
            id INT AUTO_INCREMET PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            beschreibung TEXT,
            kategorie VARCHAR(100),
            zutaten TEXT
            
        )
      """
my_cursor.execute("SHOW DATABASES")

for db in my_cursor: 
    print(db)