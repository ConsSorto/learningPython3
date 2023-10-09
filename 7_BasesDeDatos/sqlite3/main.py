import utilidades

con = utilidades.obtener_coneccion("test.db")
cursor = utilidades.obtener_cursor(con)

cursor.execute("CREATE TABLE IF NOT EXISTS Estudiantes (" +
            "id VARCHAR(11) PRIMARY KEY,"+
            "nombre1 VARCHAR(100) NOT NULL,"+
            "nombre2 VARCHAR(100) NULL,"+
            "apellido1 VARCHAR(100) NOT NULL,"+
            "apellido2 VARCHAR(100) NULL)")

cursor.execute("INSERT INTO Estudiantes VALUES('1', 'CONS',NULL ,'SORTO', 'REYES')")
 
con.commit()

datos = cursor.execute("SELECT * FROM Estudiantes").fetchall()

for dato in datos:
    print(f"id {dato[0]}\nnombre1 {dato[1]}\nnombre2 {dato[2]},\napellido1 {dato[3]},\napellido2 {dato[4]}")
