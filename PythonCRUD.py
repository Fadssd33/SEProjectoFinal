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
def Submit(nombre, raza, clase, genero, juego):
    BD.Submit(nombre, raza, clase, genero, juego)
    # Limpia datos despues de insertar los valores
    Clean()

# Funcion para leer datos
def Read():
    # Guarda los datos en una varieble llamada entries
    entries = BD.Read()
    return entries

# def Delete(ID):
#     print(ID)
    
    


# Borra los datos ingresados en los textbox
def Clean():
    txtNombre.delete(0, END)
    txtRaza.delete(0, END)
    txtClase.delete(0, END)
    txtGenero.delete(0, END)
    txtJuego.delete(0, END)

    # Regresa el foco en el primer campo
    txtNombre.focus()
## ######### Funcion para abrir ventana visualizar datos ##############
def OpenRead():
    ###### Segunda Ventana ########


    # Crea la ventana para visualizar datos
    readWindow = Tk()
    readWindow.title("Visualizar datos")
    readWindow.config(background = "#8F10CA")
    

    # crear labels para mostrar las cabeceras de los datos
    lblColumnNameID =  Label(readWindow, text="ID", bg="#FFF240", fg="black", borderwidth=3, relief="sunken", width=10)
    lblColumnNameID.grid(row=0, column=0)
    lblColumnNameNombre =  Label(readWindow, text="Nombre", bg="#FFF240", fg="black", borderwidth=3, relief="sunken", width=10)
    lblColumnNameNombre.grid(row=0, column=1)
    lblColumnNameRaza =  Label(readWindow, text="Raza", bg="#FFF240", fg="black", borderwidth=3, relief="sunken", width=10)
    lblColumnNameRaza.grid(row=0, column=2)
    lblColumnNameClase =  Label(readWindow, text="Clase", bg="#FFF240", fg="black", borderwidth=3, relief="sunken", width=10)
    lblColumnNameClase.grid(row=0, column=3)
    lblColumnNameGenero =  Label(readWindow, text="Clase", bg="#FFF240", fg="black", borderwidth=3, relief="sunken", width=10)
    lblColumnNameGenero.grid(row=0, column=4)
    lblColumnNameJuego =  Label(readWindow, text="Juego", bg="#FFF240", fg="black", borderwidth=3, relief="sunken", width=10)
    lblColumnNameJuego.grid(row=0, column=5)
    # lblColumnNameBorrar =  Label(readWindow, text="BORRAR", bg="#FF7397", fg="white", borderwidth=3, relief="sunken", width=10)
    # lblColumnNameBorrar.grid(row=0, column=6)

    # conseguir todos los datos ingresados y los pone en una varieble llamada characterList
    characterList = Read()

    
    # recorre la variable characterList y los imprime en un label
    for index, x in enumerate(characterList):
        num = 0
        for y in x:
            lblCharacter = Label(readWindow, text=y, bg="#8F10CA", fg="white", borderwidth =3, relief="sunken", width = 10)
            lblCharacter.grid(row=index + 1, column=num)
            num += 1
            
        
        # btnDeleteChar = Button(readWindow, text="BORRAR", command=lambda: Delete(x), bg="#B3AA36", fg="white", width = 10)
        # btnDeleteChar.grid(row=index + 1, column=num)

########### Funcion para abrir la ventana Borrar Datos #############3
def OpenDelete():


    # crear ventana borrado de datos
    deleteWindow = Tk()
    deleteWindow.title("Borrar registro")
    deleteWindow.config(background = "#8F10CA")
    deleteWindow.geometry("545x600")

    txtBuscarID = Entry(deleteWindow)
    txtBuscarID.grid(row=0, column=1, padx=10, pady=10)
    lblBuscarID = Label(deleteWindow, text="Buscar por ID : ")
    lblBuscarID.grid(row=0, column=0, padx=10, pady=10)
    # Boton para buscar entrada
    btnBuscarEntrada = Button(deleteWindow, text="Buscar", font= ("Cambria", 13), bg="#FFFFFF", command = lambda: BD.Delete(txtBuscarID.get()))
    btnBuscarEntrada.grid(row=0, column=3, padx=10, pady=10)
    
    
########### Funcion para abrir la ventana Actualizar Datos #############
def OpenUpdate():


    # crear ventana borrado de datos
    updateWindow = Tk()
    updateWindow.title("Actualizar registro")
    updateWindow.config(background = "#8F10CA")
    updateWindow.geometry("545x600")


    # Cajas de texto
    txtBuscarID = Entry(updateWindow)
    txtBuscarID.grid(row=0, column=1, padx=10, pady=10)
    lblBuscarID = Label(updateWindow, text="Buscar por ID : ")
    lblBuscarID.grid(row=0, column=0, padx=10, pady=10)
        # Llenar datos en los textbox
    def llenarDatos():
        # Verifica que el registro exista
        character = BD.Find(txtBuscarID.get())
        if character != None:
            # caja con el ID
            txtID = Entry(updateWindow)
            txtID.grid(row=5, column=1, padx=10, pady=10)
            txtID.insert(0, character[0])
            txtID.config(state='disabled')
            #construir la primer caja de texto
            txtNombre = Entry(updateWindow)
            txtNombre.grid(row=6, column=1, padx=10, pady=10)
            txtNombre.insert(0, character[1])
            #construir la segunda caja de texto
            txtRaza = Entry(updateWindow)
            txtRaza.grid(row=7, column=1, padx=10, pady=10)
            txtRaza.insert(0, character[2])
            #construir la tercera caja de texto
            txtClase = Entry(updateWindow)
            txtClase.grid(row=8, column=1, padx=10, pady=10)
            txtClase.insert(0, character[3])
            #construir la cuarta caja de texto
            txtGenero = Entry(updateWindow)
            txtGenero.grid(row=9, column=1, padx=10, pady=10)
            txtGenero.insert(0, character[4])
            #construir la quinta caja de texto
            txtJuego = Entry(updateWindow)
            txtJuego.grid(row=10, column=1, padx=10, pady=10)
            txtJuego.insert(0, character[5])

            # Muestra el boton para guardar cambios.
            btnGuardar = Button(updateWindow, width = 13, text="Guardar cambios", font= ("Cambria", 13), bg="#FFFFFF", command = lambda: BD.Update(txtID.get(), txtNombre.get(), txtRaza.get(), txtClase.get(), txtGenero.get(), txtJuego.get()))
            btnGuardar.grid(row=14, column=1, padx=10, pady=10)
        else:
            # Si la entrada no existe
            messagebox.showerror("Error", "El ID no existe")
    # Boton para buscar entrada
    btnBuscarEntrada = Button(updateWindow, width = 15, text="Buscar", font= ("Cambria", 13), bg="#FFFFFF", command = llenarDatos)
    btnBuscarEntrada.grid(row=0, column=3, padx=10, pady=10)


    #######    SECCION DE CREACION DE ETIQUETAS     ########
    # Etiqueta ID
    lblID = Label(updateWindow, text="ID: ", bg="#8F10CA", fg="white")
    lblID.grid(row=5, column=0, padx=10, pady=10)
    #primera etiqueta
    lblNombre = Label(updateWindow, text="Nombre : " , bg="#8F10CA", fg="white")
    lblNombre.grid(row=6, column=0, padx=10, pady=10)

    #segunda Etiqueta
    lblRaza = Label(updateWindow, text="Raza: " , bg="#8F10CA", fg="white")
    lblRaza.grid(row=7, column=0, padx=10, pady=10)

    #tercera Etiqueta
    lblClase = Label(updateWindow, text="Clase: " , bg="#8F10CA", fg="white")
    lblClase.grid(row=8, column=0, padx=10, pady=10)
    #cuarta Etiqueta
    lblGenero = Label(updateWindow, text="genero: " , bg="#8F10CA", fg="white")
    lblGenero.grid(row=9, column=0, padx=10, pady=10)
    #quinta Etiqueta
    lblJuego = Label(updateWindow, text="Juego: " , bg="#8F10CA", fg="white")
    lblJuego.grid(row=10, column=0, padx=10, pady=10)





#Creacion de la ventana principal
root = Tk()
root.title("DATOS DEl PERSONAJE")
root.config(background = "#8F10CA")
root.geometry("545x600")

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
bCrud.add_command(label="Read", command =  OpenRead)
bCrud.add_command(label="Update", command = OpenUpdate)
bCrud.add_command(label="Delete", command = OpenDelete)


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
btnCreate = Button(frmBotones, text="Crear", font= ("Cambria", 13), bg="#FFFFFF", command = lambda: Submit(txtNombre.get(), txtRaza.get(), txtClase.get(), txtGenero.get(), txtJuego.get()))
btnCreate.grid(row=0, column=0, padx=10, pady=10)
#Crear el primer boton de Leer
btnRead = Button(frmBotones, text="Leer", command=OpenRead, font= ("Cambria", 13), bg="#FFFFFF")
btnRead.grid(row=0, column=1, padx=10, pady=19)
#Crear el primer boton de Actualizar
btnUpdate = Button(frmBotones, text="Actualizar", command=OpenUpdate, font= ("Cambria", 13), bg="#FFFFFF")
btnUpdate.grid(row=0, column=2, padx=10, pady=10)
#Crear el primer boton de borrar
btnDelete = Button(frmBotones, text="Borrar", command=OpenDelete, font= ("Cambria", 13), bg="#FFFFFF")
btnDelete.grid(row=0, column=3, padx=10, pady=10)




#Creamos un bucle
root.mainloop()