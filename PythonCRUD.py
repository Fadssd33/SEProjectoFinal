#importar las librerias
from tkinter import *
from tkinter import messagebox
import sqlite3

######### En esta seccion se crean las funciones del sistema
# Creamos la funcion para crear la base de datos
def conectarBD():
    #variables: conexcion y cursor
    myconexion = sqlite3.connect("dbalumnos")
    mycursor = myconexion.cursor()

    try:
        mycursor.execute('''CREATE TABLE detalleAlumnos
        (numExpediente INTEGER PRIMARY KEY,
        aPaterno VARCHAR (40),
        aMaterno VARCHAR (40),
        nombre VARCHAR (50))''')
        # Notificamos al usuario que la base de datos ha sido creada
        messagebox.showinfo("D.B","La base de datos ha sido creada con exito!")
    except:
        messagebox.showerror("D.B","La base de datos ya existe!")
        
# Creamos la funcion para salir del sistema
def SalirSistema():
    #Mandar un mensaje
    respuesta = messagebox.askquestion("Cerrar Sistema", "¿Deseas cerrar el sistema?")
    #estructura condicionante que me permita evaluar la respuesta
    if respuesta == "yes":
        root.destroy()
    else:
        pass


#Creacion de la ventana principal
root = Tk()
root.title("DATOS DE ALUMNOS")
root.config(background = "#8F10CA")

#Crear la barra del menu
barraMenu = Menu (root)


#Configurar los parametros de la ventana principal
root.config(menu = barraMenu, height = 200, width = 400)


# Contruiremos la primer opción del menú
bConexion = Menu(barraMenu, tearoff = 0)
bConexion.add_command(label="Conexion Base de Datos (B.D)", command=conectarBD)
bConexion.add_command(label="Salir..." , command=SalirSistema)


#Contruiremos la segunda opción del menú
bLimpiar=Menu(barraMenu, tearoff = 0)
bLimpiar.add_command(label="Limpiar campos")


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
txtExpediente = Entry(frmEntryLabel)
txtExpediente.grid(row=0, column=1, padx=10, pady=10)

#construir la primer caja de texto
txtApellidoPaterno = Entry(frmEntryLabel)
txtApellidoPaterno.grid(row=1, column=1, padx=10, pady=10)

#construir la primer caja de texto
txtApellidoMaterno = Entry(frmEntryLabel)
txtApellidoMaterno.grid(row=2, column=1, padx=10, pady=10)

#construir la primer caja de texto
txtNombreAlumno = Entry(frmEntryLabel)
txtNombreAlumno.grid(row=3, column=1, padx=10, pady=10)

#######    SECCION DE CREACION DE ETIQUETAS     ########

lblExpediente = Label(frmEntryLabel, text="Numero de Expediente: " , bg="#8F10CA", fg="white" )
lblExpediente.grid(row=0, column=0, padx=10, pady=10)

#segunda etiqueta
lblApellidoPaterno = Label(frmEntryLabel, text="Apellido Paterno: " , bg="#8F10CA", fg="white")
lblApellidoPaterno.grid(row=1, column=0, padx=10, pady=10)

#tercera Etiqueta
lblApellidoMaterno = Label(frmEntryLabel, text="Apellido Materno: " , bg="#8F10CA", fg="white")
lblApellidoMaterno.grid(row=2, column=0, padx=10, pady=10)

#cuarta Etiqueta
lblNombreAlumno = Label(frmEntryLabel, text="Apellido Materno: " , bg="#8F10CA", fg="white")
lblNombreAlumno.grid(row=3, column=0, padx=10, pady=10)


############ constrir el fame que contendra : los botpnes que invocan las funciones C-R-U-D  #
# Crear el frame    
frmBotones = Frame(root)
frmBotones.pack()
frmBotones.config(background="#8F10CA")
#Crear el primer boton de crear
btnCreate = Button(frmBotones, text="Crear", font= ("Cambria", 13), bg="#FFFFFF")
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