query_all = "SELECT * FROM Mietwagen"

insert_car = "INSERT INTO Mietwagen (Marke, Modell, Farbe, Motorleistung, Antriebsart, Baujahr, `Mietpreis pro tag`) Values (%s, %s, %s, %s, %s, %s, %s)"
query_search_mark = "SELECT * FROM Mietwagen WHERE Marke = %s"
query_search_model = "SELECT * FROM Mietwagen WHERE Modell = %s"
query_search_drivetype = "SELECT * FROM Mietwagen WHERE Antriebsart = %s"
