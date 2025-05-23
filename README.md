# efs2b_datenbank

# Vorraussetzungen

Folgende Abhängigkeiten sind nötig um die Datenbankverwaltung zu benutzen:

- MYSQL(oder wahlweise MariaDB) müssen auf dem System installiert sein
- Python3 muss installiert sein
- Der MYSQL Connector muss über pip installiert worden sein
- Das Modell zu finden im Ordner `datenbank` muss über die Workbench in die Datenbank importiert werden

# Anpassungen Code

Der Name meiner Datenbank ist `Projektarbeit` sollte eure Datenbank einen anderen Namen haben müsst ihr diesen anpassen.
Nutzername und Password sind jeweils `admin` und `admin` auch hier müsst ihr die Werte ändern wenn sie bei euch anders sind.

Durchführung der Änderungen:

Öffnet die Datei `src/database.py`

Springt zu Zeile 7
```
context = mysql.connector.connect(host="localhost", password="admin", user="admin", db="Projektarbeit", charset="utf8mb4")
```

Hier passt ihr die jeweiligen Werte an  z.b. eure Datenbank heißt `Autoverleih` dann müsst ihr die Zeile wie folgt anpassen:
```
context = mysql.connector.connect(host="localhost", password="admin", user="admin", db="Autoverleih", charset="utf8mb4")
```
