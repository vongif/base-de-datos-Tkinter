from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
import sqlite3
import re

# BASE SQLITE--------------------------------------------------------------------------


def base():
    con = sqlite3.connect("base_ejemplo.db")
    return con


def crear_tabla():
    con = base()
    cursor = con.cursor()
    sql = """CREATE TABLE clientes (cuenta INTERGER, reparto INTERGER, numero_de_cliente INTERGER PRIMARY KEY, razonsocial VARCHAR, direccion VARCHAR, localidad VARCHAR)"""
    cursor.execute(sql)
    con.commit()


try:
    base()
    crear_tabla()
except:
    print("Hay un error")


def funcion_alta(
    cuenta, reparto, numero_de_cliente, razonsocial, direccion, localidad, tree
):
    cuenta = valor_cuenta.get()
    reparto = valor_reparto.get()
    numero_de_cliente = valor_cliente.get()
    razonsocial = valor_razon.get()
    direccion = valor_direccion.get()
    localidad = valor_localidad.get()
    regex = valor_razon.get()
    expresion = "[a-zA-Z0-9_]"
    if re.match(expresion, regex):
        Label(mensaje, text="Registro valido", font="Courier, 10", fg="blue2").place(
            x=280, y=100
        )
        con = base()
        cursor = con.cursor()
        data = (cuenta, reparto, numero_de_cliente, razonsocial, direccion, localidad)
        sql = "INSERT INTO clientes(cuenta, reparto, numero_de_cliente, razonsocial, direccion, localidad) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        tree.insert(
            "",
            "end",
            values=(
                valor_cuenta.get(),
                valor_reparto.get(),
                valor_cliente.get(),
                valor_razon.get(),
                valor_direccion.get(),
                valor_localidad.get(),
            ),
        )
    else:
        Label(
            mensaje,
            text="Invalido. Registro solo alfanumerico",
            font="Courier, 10",
            fg="red2",
        ).place(x=280, y=100)
    actualizar(tree)
    limpiar_registro()


def limpiar_registro():
    valor_cuenta.set(""), valor_reparto.set(""), valor_cliente.set(""), valor_razon.set(
        ""
    ), valor_direccion.set(""), valor_localidad.set("")


def funcion_borrar(tree):
    if askyesno("Base Clientes", "Desea eliminar el registro?"):
        cliente = tree.selection()
        print(cliente)
        item = tree.item(cliente)
        print(item)
        print(item["text"])
        mi_id = item["text"]
        con = base()
        cursor = con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM clientes WHERE cuenta = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(cliente)
        showinfo("Base Clientes", "Registro eliminado")
    else:
        showinfo("No", "No se eliminara el registro")


def actualizar(tree):
    records = tree.get_children()
    for element in records:
        tree.delete(element)
        sql = "SELECT * FROM clientes ORDER BY cuenta ASC"
    con = base()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        tree.insert(
            "",
            "end",
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4], fila[5]),
        )


def funcion_modificar(tree):
    if askyesno("Base Clientes", "Desea modificar el registro?"):
        cliente = tree.selection()
        item = tree.item(cliente)
        mi_id = item["text"]
        con = base()
        cursor = con.cursor()
        sql = f"UPDATE clientes SET cuenta = '{valor_cuenta.get()}', reparto = '{valor_reparto.get()}', numero_de_cliente = '{valor_cliente.get()}', razonsocial = '{valor_razon.get()}', direccion = '{valor_direccion.get()}', localidad = '{valor_localidad.get()}' WHERE cuenta = '?';"
        cursor.execute(sql)
        con.commit()
        funcion_alta(
            cuenta, reparto, numero_de_cliente, razonsocial, direccion, localidad, tree
        )
        showinfo("Base Clientes", "Registro modificado")
    else:
        showinfo("No", "No se modificara el registro")


aplicacion = Tk()

titulo = Label(
    aplicacion,
    text="BASE CLIENTES",
    bg="Grey49",
    fg="white",
    height=1,
    width=55,
    font=("bold"),
)
titulo.grid(row=0, column=0, columnspan=7, padx=1, pady=1, sticky=W + E)

cuenta = Label(aplicacion, text="Cuenta :", fg="black", anchor="center")
cuenta.grid(row=1, column=0, sticky=W)
reparto = Label(aplicacion, text="Reparto :", fg="black", anchor="center")
reparto.grid(row=2, column=0, sticky=W)
numero_de_cliente = Label(
    aplicacion,
    text="Numero de Cliente : ",
    fg="black",
    anchor="center",
)
numero_de_cliente.grid(row=3, column=0, sticky=W)
razonsocial = Label(aplicacion, text="Razon Social : ", fg="black", anchor="center")
razonsocial.grid(row=4, column=0, sticky=W)
direccion = Label(aplicacion, text="Direccion : ", fg="black", anchor="center")
direccion.grid(row=5, column=0, sticky=W)
localidad = Label(aplicacion, text="Localidad :", fg="black", anchor="center")
localidad.grid(row=6, column=0, sticky=W)

mensaje = ()
valor_cuenta = IntVar()
valor_reparto = IntVar()
valor_cliente = IntVar()
valor_razon = StringVar()
valor_direccion = StringVar()
valor_localidad = StringVar()


entry_cuenta = Entry(aplicacion, textvariable=valor_cuenta, width=15)
entry_cuenta.grid(row=1, column=0)
entry_reparto = Entry(aplicacion, textvariable=valor_reparto, width=15)
entry_reparto.grid(row=2, column=0)
entry_numero_de_cliente = Entry(aplicacion, textvariable=valor_cliente, width=15)
entry_numero_de_cliente.grid(row=3, column=0)
entry_razonsocial = Entry(aplicacion, textvariable=valor_razon, width=30)
entry_razonsocial.grid(row=4, column=0)
entry_direccion = Entry(aplicacion, textvariable=valor_direccion, width=30)
entry_direccion.grid(row=5, column=0)
entry_localidad = Entry(aplicacion, textvariable=valor_localidad, width=30)
entry_localidad.grid(row=6, column=0)


# -------------------------------------------------
# TREEVIEW
# -------------------------------------------------

tree = ttk.Treeview(aplicacion)

aplicacion.geometry("1060x700")

entrybusqueda = ttk.Entry(aplicacion)
entrybusqueda.grid(row=9, column=0, padx=5, pady=5, ipady=3, ipadx=60)

s = ttk.Style()
s.theme_use("clam")
s.configure("Treeview.Heading", background="Grey49")
s.configure(
    "Treeview",
    background="grey74",
    fieldbackground="grey74",
    foreground="black",
)

tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=50, minwidth=0, anchor=W)
tree.column("col1", width=50, minwidth=80, anchor=W)
tree.column("col2", width=150, minwidth=80, anchor=W)
tree.column("col3", width=300, minwidth=80, anchor=W)
tree.column("col4", width=300, minwidth=80, anchor=W)
tree.column("col5", width=200, minwidth=80, anchor=W)


tree.heading("#0", text="Cuenta")
tree.heading("col1", text="Reparto")
tree.heading("col2", text="Numero de Cliente")
tree.heading("col3", text="Razon Social")
tree.heading("col4", text="Direccion")
tree.heading("col5", text="Localidad")

tree.grid(column=0, row=20, columnspan=5, ipady=100)

boton_guardar = Button(
    aplicacion,
    text="Alta",
    bg="Grey49",
    fg="white",
    padx=71,
    pady=3,
    command=lambda: funcion_alta(
        cuenta, reparto, numero_de_cliente, razonsocial, direccion, localidad, tree
    ),
)
boton_guardar.grid(row=3, column=2)
boton_borrar = Button(
    aplicacion,
    text="Eliminar",
    bg="Grey49",
    fg="white",
    padx=60,
    pady=3,
    command=lambda: funcion_borrar(tree),
)
boton_borrar.grid(row=4, column=2)
boton_salir = Button(
    aplicacion,
    text="Salir",
    bg="Grey49",
    fg="white",
    padx=60,
    pady=3,
    command=aplicacion.quit,
)
boton_salir.grid(row=7, column=3)
boton_modificar = Button(
    aplicacion,
    text="Modificar",
    bg="Grey49",
    fg="white",
    padx=56,
    pady=3,
    command=lambda: funcion_modificar(tree),
)
boton_modificar.grid(row=5, column=2)
boton_actualizar = Button(
    aplicacion,
    text="Actualizar",
    bg="Grey49",
    fg="white",
    padx=56,
    pady=3,
    command=lambda: actualizar(tree),
)
boton_actualizar.grid(row=6, column=2)


aplicacion.mainloop()
