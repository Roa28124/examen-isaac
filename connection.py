import pyodbc

def obtener_cadena(SERVER, DATABASE):
    return f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'

def conectar(SERVER, DATABASE):
    cadena = obtener_cadena(SERVER, DATABASE)
    try:
        connection = pyodbc.connect(cadena)
        print("Conexion exitosa")
        return connection
    except pyodbc.Error as err:
        print(f'Error: {err}')
        return None
    
def cerrar_conexion(connection):
    if connection:
        connection.close()
        print('Conexion cerrada')