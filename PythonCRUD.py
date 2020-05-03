#importar las librerias
import CRUDFunctions as BD
from tkinter import *
from tkinter import messagebox
import sqlite3



# Creamos la funcion para salir del sistema
def SalirSistema():
    #Mandar un mensaje
    respuesta = messagebox.askquestion("Cerrar Sistema", "¿Deseas cerrar el sistema?")
    #estructura condicionante que me permita evaluar la respuesta
    if respuesta == "yes":
        root.destroy()
    else:
        pass

# Funcion insertar datos
def Submit():
    nombre = txtNombre.get()
    raza = txtRaza.get()
    clase = txtClase.get()
    genero = txtGenero.get()
    juego = txtJuego.get()
    

    BD.Submit(nombre, raza, clase, genero, juego)
    Clean()
# Borra los datos ingresados en los textbox
def Clean():
    txtNombre.delete(0, END)
    txtRaza.delete(0, END)
    txtClase.delete(0, END)
    txtGenero.delete(0, END)
    txtJuego.delete(0, END)

    # Regresa el foco en el primer campo
    txtNombre.focus()
    
#Creacion de la ventana principal
root = Tk()
root.title("DATOS DEl PERSONAJE")
root.config(background = "#8F10CA")

#Crear la barra del menu
barraMenu = Menu (root)


#Configurar los parametros de la ventana principal
root.config(menu = barraMenu, height = 200, width = 400)


# Contruiremos la primer opción del menú
bConexion = Menu(barraMenu, tearoff = 0)
bConexion.add_command(label="Conexion Base de Datos (B.D)", command=BD.conectarBD)
bConexion.add_command(label="Salir..." , command=SalirSistema)


#Contruiremos la segunda opción del menú
bLimpiar=Menu(barraMenu, tearoff = 0)
bLimpiar.add_command(label="Limpiar campos", command = Clean)


#Contruiremos la tercera opción del menú
bCrud = Menu(barraMenu, tearoff = 0)
bCrud.add_command(label="Create")
bCrud.add_command(label="Read")
bCrud.add_command(label="Update")
bCrud.add_command(label="Delete")


#Contruiremos la cuarta opción del menú
bAyuda = Menu(barraMenu, tearoff = 0)
bAyuda.add_command(label="Ayuda...")
bAyuda.add_command(label="Acerca de...")


##### Asignamos las opciones creadas al menu
barraMenu.add_cascade(label="CONEXIÓN B.D", menu=bConexion)
barraMenu.add_cascade(label="LIMPIAR", menu=bLimpiar)
barraMenu.add_cascade(label="C-R-U-D", menu=bCrud)
barraMenu.add_cascade(label="AYUDA", menu=bAyuda)

###################En esta seccion contrimos el frame que contendra : cajas de texto y etiquetas
#contrccion de frame
frmEntryLabel = Frame(root)
frmEntryLabel.pack()
frmEntryLabel.config(background="#8F10CA")

#construir la primer caja de texto
# txtExpediente = Entry(frmEntryLabel)
# txtExpediente.grid(row=0, column=1, padx=10, pady=10)

#construir la primer caja de texto
txtNombre = Entry(frmEntryLabel)
txtNombre.grid(row=0, column=1, padx=10, pady=10)
#construir la segunda caja de texto
txtRaza = Entry(frmEntryLabel)
txtRaza.grid(row=1, column=1, padx=10, pady=10)
#construir la tercera caja de texto
txtClase = Entry(frmEntryLabel)
txtClase.grid(row=2, column=1, padx=10, pady=10)
#construir la cuarta caja de texto
txtGenero = Entry(frmEntryLabel)
txtGenero.grid(row=3, column=1, padx=10, pady=10)
#construir la quinta caja de texto
txtJuego = Entry(frmEntryLabel)
txtJuego.grid(row=4, column=1, padx=10, pady=10)

#######    SECCION DE CREACION DE ETIQUETAS     ########

# lblExpediente = Label(frmEntryLabel, text="Numero de Expediente: " , bg="#8F10CA", fg="white" )
# lblExpediente.grid(row=0, column=0, padx=10, pady=10)

#primera etiqueta
lblNombre = Label(frmEntryLabel, text="Nombre : " , bg="#8F10CA", fg="white")
lblNombre.grid(row=0, column=0, padx=10, pady=10)

#segunda Etiqueta
lblRaza = Label(frmEntryLabel, text="Raza: " , bg="#8F10CA", fg="white")
lblRaza.grid(row=1, column=0, padx=10, pady=10)

#tercera Etiqueta
lblClase = Label(frmEntryLabel, text="Clase: " , bg="#8F10CA", fg="white")
lblClase.grid(row=2, column=0, padx=10, pady=10)
#cuarta Etiqueta
lblGenero = Label(frmEntryLabel, text="genero: " , bg="#8F10CA", fg="white")
lblGenero.grid(row=3, column=0, padx=10, pady=10)
#quinta Etiqueta
lblJuego = Label(frmEntryLabel, text="Juego: " , bg="#8F10CA", fg="white")
lblJuego.grid(row=4, column=0, padx=10, pady=10)


############ constrir el fame que contendra : los botones que invocan las funciones C-R-U-D  #
# Crear el frame    
frmBotones = Frame(root)
frmBotones.pack()
frmBotones.config(background="#8F10CA")
#Crear el primer boton de crear
btnCreate = Button(frmBotones, text="Crear", font= ("Cambria", 13), bg="#FFFFFF", command = Submit)
btnCreate.grid(row=0, column=0, padx=10, pady=10)
#Crear el primer boton de Leer
btnRead = Button(frmBotones, text="Leer", font= ("Cambria", 13), bg="#FFFFFF")
btnRead.grid(row=0, column=1, padx=10, pady=19)
#Crear el primer boton de Actualizar
btnUpdate = Button(frmBotones, text="Actualizar", font= ("Cambria", 13), bg="#FFFFFF")
btnUpdate.grid(row=0, column=2, padx=10, pady=10)
#Crear el primer boton de borrar
btnDelete = Button(frmBotones, text="Borrar", font= ("Cambria", 13), bg="#FFFFFF")
btnDelete.grid(row=0, column=3, padx=10, pady=10)

#Creamos un bucle
root.mainloop()