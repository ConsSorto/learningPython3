import sqlite3

def obtener_coneccion(base):
    con = sqlite3.connect(base)
    return con

def obtener_cursor(con):
    cursor = con.cursor()
    return cursor




