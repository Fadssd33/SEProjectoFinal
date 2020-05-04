import sqlite3
from tkinter import messagebox
import CRUDFunctions as BD

# Conexion a base de datos
def conectarBD():
    # Variable de conexion
    myconexion = sqlite3.connect("dbRPG")

    # Variable de cursor
    c = myconexion.cursor()

    # Hacer cambios en la base de datos
    myconexion.commit()

   

    try:
        # Si no existe la tabla la crea
        c.execute('''CREATE TABLE characterDetails
        (id INTEGER PRIMARY KEY,
        nombre VARCHAR (40),
        raza VARCHAR (40),
        clase VARCHAR (40),
        genero VARCHAR (50),
        juego VARCHAR (30)
        )''')
        # Notificamos al usuario que la base de datos ha sido creada
        messagebox.showinfo("D.B","La base de datos ha sido creada con exito!")
        
    except:
        # Si ya existe manda una mensaje al usuario
        messagebox.showerror("D.B","La base de datos ya existe!")

    # Cerrar conexion
        myconexion.close()
       

# Funcion para agregar entradas
def Submit(nombre, raza, clase, genero, juego):

    # Verifica que si no hay datos vacios
    if (nombre == "" or raza == "" or clase == "" or genero == "" or juego == ""):
        messagebox.showerror("ERROR", "Alguno de los datos esta vacio, intentelo de nuevo")
    else: 
        myconexion = sqlite3.connect("dbRPG")

        # Variable de cursor
        c = myconexion.cursor()

        # Insertar datos en la tabla
        c.execute("INSERT INTO characterDetails VALUES (null, '" + nombre + "', '"+ raza + "', '" + clase + "', '" + genero + "', '" + juego + "')")
        # Hacer cambios en la base de datos
        myconexion.commit()
        messagebox.showinfo('B.D', 'Personaje agregado con exito')
        # Cerrar conexion
        myconexion.close()

# Funcion para leer datos ingresados
def Read():
    myconexion = sqlite3.connect("dbRPG")

    # Variable de cursor
    c = myconexion.cursor()

    # Executa comando para leer datos
    c.execute("SELECT * FROM characterDetails")
    # Consigue todas las entradas
    records = c.fetchall()
    
    print_records = ''
    # Convertir todos los datos en strings y luego imprimirlos
    recordsList = []
    for x in records:
        recordsList.append(x)
    # regresa todos las entradas
    return recordsList

    myconexion.commit()
    # Cerrar conexion
    myconexion.close()


# Funcion para borrar un registro
def Delete(ID):
    myconexion = sqlite3.connect("dbRPG")

    # Buscar el valor de personaje y guardarlo en la variable character
    character = Find(ID)
    
    # Verifica que el registro exista
    if character == None:
        messagebox.showerror("Error", "El registro no existe")
        pass
    # Si el registro si existe:
    else:
            # Pregunta al usuario si desea borrar los datos
        result = messagebox.askyesno(title="Confirmar borrado de datos", message="Esta seguro que desea borrar el siguiente registro: \n " + str(character))
    
        if result == True:
            # Variable de cursor
            c = myconexion.cursor()
        

            # Query parra borrar un registro
            c.execute("DELETE from characterDetails WHERE id = '"+ ID + "'")
            myconexion.commit()
            # Cerrar conexion
            myconexion.close()
    # Si el usuario presiona no:
        else: 
            pass

# Funcion para cambiar datos de un registro
def Update(id, nombre, raza, clase, genero, juego):

    myconexion = sqlite3.connect("dbRPG")
    c = myconexion.cursor()

    try:
       # Si la query se ejecuta correctamente
       c.execute("UPDATE characterDetails SET nombre = '" + nombre + "', raza = '" + raza + "', clase = '" + clase + "', genero = '" + genero + "', juego = '" + juego + "' WHERE id = " + id)
       messagebox.showinfo("BIEN", "Datos actualizados con exito")
       
        
    except:
        # Si no se pudieron ingresar los datos
        messagebox.showerror("ERROR", "Los datos no pudieron ser ingresados")
        



    myconexion.commit()
    # Cerrar conexion
    myconexion.close()
    

    


# Funcion para Encontrar un registro
def Find(ID):
    myconexion = sqlite3.connect("dbRPG")

    # Variable de cursor
    c = myconexion.cursor()

    # Query para recuperar un registro por el ID
    c.execute("SELECT * FROM characterDetails WHERE id = '" + ID +"'")
    # Regresa los valores que estan en la fila
    return c.fetchone()
 
    myconexion.commit()
    # Cerrar conexion
    myconexion.close()
