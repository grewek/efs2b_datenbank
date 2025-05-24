query_all = "SELECT Mietwagennr, Marke, Modell, Farbe, Motorleistung, Antriebsart, Baujahr, `Mietpreis pro tag` FROM Mietwagen"

insert_car = ("INSERT INTO Mietwagen "
    "(Marke, Modell, Farbe, Motorleistung, Antriebsart, Baujahr, `Mietpreis pro tag`) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

#Queries zum Updaten von Datenbankeinträgen.
update_car_mark = ("UPDATE Mietwagen SET Marke = %s WHERE Mietwagennr = %s")
update_car_model = ("UPDATE Mietwagen SET Modell = %s WHERE Mietwagennr = %s")
update_car_color = ("UPDATE Mietwagen SET Farbe = %s WHERE Mietwagennr = %s")
update_car_drive_type = ("UPDATE Mietwagen SET Antriebsart = %s WHERE Mietwagennr = %s")
update_car_manufacture_date = ("UPDATE Mietwagen SET Baujahr = %s WHERE Mietwagennr = %s")
update_car_price = ("UPDATE Mietwagen SET `Mietpreis pro tag` = %s WHERE Mietwagennr = %s")
update_car_power = ("UPDATE Mietwagen SET Leistung = %s WHERE Mietwagennr = %s ")

query_search_mark = "SELECT * FROM Mietwagen WHERE Marke = %s"
query_search_model = "SELECT * FROM Mietwagen WHERE Modell = %s"
query_search_drivetype = "SELECT * FROM Mietwagen WHERE Antriebsart = %s"
query_search_price_asc = "SELECT * FROM Mietwagen ORDER BY `Mietpreis pro Tag`"
query_search_price_desc = "SELECT * FROM Mietwagen ORDER BY `Mietpreis pro Tag` DESC"
