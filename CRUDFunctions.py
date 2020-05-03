import sqlite3
from tkinter import messagebox

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

# Agregar personaje a la base de datos
### INSERT ###


