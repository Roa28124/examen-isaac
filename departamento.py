import pyodbc
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def añadir(connection): 
    cursor = connection.cursor()
    while True:
        try:
            id_departamento= int(input('Ingrese el ID de la departamento: '))
            break
        except ValueError:
            print('Solo se permiten números. Intente de nuevo.')

    # Ingreso del nombre de la biblioteca
    nombre_departamento = input('Ingrese el nombre de la departamento: ')

    # Ingreso de la ubicación de la biblioteca
    ubicacion_departamento = input('Ingrese la ubicación del departamento: ')

    # Inserción de la biblioteca en la base de datos
    try:
        cursor.execute('INSERT INTO Departamentos (DepartamentoID, Nombre, Ubicacion) VALUES (?, ?, ?)', id_departamento, nombre_departamento, ubicacion_departamento)
        connection.commit()
        print('departamento gregada correctamente.')
    except pyodbc.Error as err:
        print(f'Error al agregar la departamento: {err}')

    # Cierre de la conexión y mensaje final
    cursor.close()
    connection.close()
    input(' continuar')

def mostrar(connection):
    try:
        cursor = connection.cursor()
       
        query='SELECT DepartamentoID, Nombre, Ubicacion FROM Departamentos'
       
        cursor.execute(query)
        departamentos=cursor.fetchall()

        for i in departamentos:
            print(f'ID: {i[0]} - Nombre: {i[1]} - Ubicacion: {i[2]}')
        input('continuar ')
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input(' continuar')
def actualizar(connection):
    try:
        cursor=connection.cursor()
        id=None
        while id == None:
            id= input("Ingrese el id del departamento que desea actualizar: ")
            
            if not id.isdigit():
                input("Error el dato debe ser un numero")
                id=None
                continue
        id= int(id)
        clear()
        r=None
        while r==None:
            print("1-nombre \n2-ubicación \n3-Todos")
            respuesta=int(input("ingrese una opcion"))
            match respuesta:
                case 1: 
                    nombre=input("ingrese el nombre nuevo: ")
                    query=  query = 'UPDATE Departamentos SET Nombre = ? WHERE DepartamentoID = ?'
                    cursor.execute(query,nombre,id)
                    print("Actualizado con exito")
                    input("Dale enter para continuar")
                    return
                case 2: 
                    ubicacion =input("ingrese la ubicacion nueva : ")
                    query=  query = 'UPDATE Departamentos SET Nombre = ? WHERE DepartamentoID = ?'
                    cursor.execute(query,nombre,id)
                    print("Actualizado con exito")
                    input("Dale enter para continuar")
                    return
                case 3: 
                    nombre=input("ingrese el nombre nuevo:")
                    ubicacion =input("ingrese la ubicacion nueva : ")
                    query = 'UPDATE Departamentos SET Nombre = ?, Ubicacion = ? WHERE DepartamentoID = ?'  
                    cursor.execute(query, nombre, ubicacion, id)
                    print("Actualizado con exito")
                    input("Dale enter para continuar")
                    return
            connection.commit()   
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('continuar')          
def eliminar(connection):
    try:
        cursor = connection.cursor()
        id = None
        while id == None:
            id = input('Ingrese el id del departamento: ')
            if not id.isdigit():
                input('Solo puede ingresar numeros, intente nuevamente')
                id = None
                continue
        id = int(id)
        cursor.execute(f'DELETE FROM departamentos WHERE DepartamentoID = {id}')
        connection.commit()
        input('Departamento eliminado exitosamente')
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')
            