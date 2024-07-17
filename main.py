from db.connection import *
from db.departamento import *

SERVER = 'DESKTOP-OOM576D\SQLEXPRESS'
DATABASE = 'Escuela'
TABLE = 'Departamentos'

def main():
    try:
        connection = conectar(SERVER, DATABASE)
        cursor = connection.cursor()
        p = None
        while p == None:
            print("1-añadir \n2-Mostrar \n3-Actualizar \n4-Eliminar \n5-salir")
            menu= (input("Escoja una opcion "))
            if not menu.isdigit():
                print("Ingrese un numero valido")
                input("dale enter para continuar")
                os.system('cls')
                continue
            menu=int(menu)
            
                

            match menu:
                case 1:
                    os.system('cls')
                    añadir(connection)
                case 2:
                    os.system('cls')
                    mostrar(connection)  
                case 3:  
                    os.system('cls')
                    actualizar(connection)
                case 4:
                    os.system('cls')
                    eliminar(connection)    
                case 5: 
                    break  
                case default:
                    print("ingrese una opcion")    
                    input("dale enter para continuar")
                    os.system('cls')
                    continue

    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione enter')
if __name__ == '__main__':
    main()