from tkinter import IntVar
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
import tkinter as tk
from modelo import base
from modelo import crear_tabla
from modelo import funcion_actualizar
from modelo import funcion_alta
from modelo import funcion_borrar
from modelo import funcion_modificar
from modelo import funcion_buscar
from modelo import funcion_imprimir


def vista_principal(aplicacion):

    #aplicacion = Tk()

    valor_cuenta = IntVar()
    valor_reparto = IntVar()
    valor_cliente = IntVar()
    valor_sucursal = IntVar()
    valor_razon = StringVar()
    valor_direccion = StringVar()
    valor_localidad = StringVar()
    valor_busqueda = StringVar()


    titulo = Label(
    aplicacion,
    text="BASE CLIENTES",
    bg="Grey49",
    fg="white",
    height=1,
    width=55,
    font=("bold"),
    )
    titulo.grid(row=0, column=0, columnspan=7, padx=1, pady=1, sticky="w" + "e")


    cuenta = Label(aplicacion, text="Cuenta :", fg="black", anchor="center")
    cuenta.grid(row=1, column=0, sticky="w")
    reparto = Label(aplicacion, text="Reparto :", fg="black", anchor="center")
    reparto.grid(row=2, column=0, sticky="w")
    numero_de_cliente = Label(
    aplicacion,
    text="Numero de Cliente : ",
    fg="black",
    anchor="center",
    )
    numero_de_cliente.grid(row=3, column=0, sticky="w")
    sucursal = Label(
    aplicacion,
    text="Sucursal:",
    fg="black",
    anchor="center",
    )
    sucursal.grid(row=3, column=0, sticky="e")
    razonsocial = Label(aplicacion, text="Razon Social : ", fg="black", anchor="center")
    razonsocial.grid(row=4, column=0, sticky="w")
    direccion = Label(aplicacion, text="Direccion : ", fg="black", anchor="center")
    direccion.grid(row=5, column=0, sticky="w")
    localidad = Label(aplicacion, text="Localidad :", fg="black", anchor="center")
    localidad.grid(row=6, column=0, sticky="w")

    entry_cuenta = Entry(aplicacion, textvariable=valor_cuenta, width=15)
    entry_cuenta.grid(row=1, column=0)
    entry_reparto = Entry(aplicacion, textvariable=valor_reparto, width=15)
    entry_reparto.grid(row=2, column=0)
    entry_numero_de_cliente = Entry(aplicacion, textvariable=valor_cliente, width=15)
    entry_numero_de_cliente.grid(row=3, column=0)
    entry_sucursal = Entry(aplicacion, textvariable=valor_sucursal, width=5)
    entry_sucursal.grid(row=3, column=1, sticky="w")
    entry_razonsocial = Entry(aplicacion, textvariable=valor_razon, width=30)
    entry_razonsocial.grid(row=4, column=0)
    entry_direccion = Entry(aplicacion, textvariable=valor_direccion, width=30)
    entry_direccion.grid(row=5, column=0)
    entry_localidad = Entry(aplicacion, textvariable=valor_localidad, width=30)
    entry_localidad.grid(row=6, column=0)
    entrybusqueda = ttk.Entry(aplicacion, textvariable=valor_busqueda)
    entrybusqueda.grid(row=9, column=0, padx=55, pady=8, ipady=3, ipadx=60)


    # -------------------------------------------------
    # TREEVIEW
    # -------------------------------------------------


    tree = ttk.Treeview(aplicacion)

    aplicacion.geometry("1125x700")

    scroll = ttk.Scrollbar(aplicacion)
    scroll.place(x=1105, y=289, height=405, width=25)
    tree.config(yscrollcommand=scroll.set)
    scroll.config(command=tree.yview)


    s = ttk.Style()
    s.theme_use("clam")
    s.configure("Treeview.Heading", background="Grey49", bg="white", fg="white")
    s.configure(
    "Treeview",
    background="grey74",
    fieldbackground="grey74",
    foreground="black",
    )
    s.configure(
    "Vertical.TScrollbar",
    gripcount=6,
    background="White",
    darkcolor="Black",
    troughcolor="gray78",
    bordercolor="Black",
    arrowcolor="gray36",
    )


    tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
    tree.column("#0", width=50, minwidth=80, anchor="center")
    tree.column("col1", width=50, minwidth=80, anchor="center")
    tree.column("col2", width=130, minwidth=80, anchor="center")
    tree.column("col3", width=50, minwidth=80, anchor="center")
    tree.column("col4", width=300, minwidth=80, anchor="w")
    tree.column("col5", width=290, minwidth=80, anchor="w")
    tree.column("col6", width=230, minwidth=80, anchor="w")

    tree.heading("#0", text="Cuenta")
    tree.heading("col1", text="Reparto")
    tree.heading("col2", text="Numero de Cliente")
    tree.heading("col3", text="Sucursal")
    tree.heading("col4", text="Razon Social")
    tree.heading("col5", text="Direccion")
    tree.heading("col6", text="Localidad")

    tree.grid(column=0, row=20, columnspan=5, ipady=100)

    def aviso_alta(
    valor_cuenta,
    valor_reparto,
    valor_cliente,
    valor_sucursal,
    valor_razon,
    valor_direccion,
    valor_localidad,
    tree,
    ):

        retorno = funcion_alta(
        valor_cuenta,
        valor_reparto,
        valor_cliente,
        valor_sucursal,
        valor_razon,
        valor_direccion,
        valor_localidad,
        tree,
        )
        if messagebox.showinfo("Base Clientes", retorno):
            Label(aplicacion, text="Registro valido", font="Courier, 10", fg="blue2").place(
            x=280, y=100
            )
        else:
            messagebox.showinfo("Base Clientes", retorno)


    boton_alta = Button(
    aplicacion,
    text="Alta",
    bg="Grey49",
    fg="white",
    padx=71,
    pady=3,
    command=lambda: aviso_alta(
    valor_cuenta,
    valor_reparto,
    valor_cliente,
    valor_sucursal,
    valor_razon,
    valor_direccion,
    valor_localidad,
    tree,
    ),
    )
    boton_alta.grid(row=3, column=2)


    def aviso_borrar(tree):
        retorno = funcion_borrar(tree)
        # Label(
        # aplicacion, text="Registro Eliminado", font="Courier, 15", fg="blue2"
        # ).place(x=400, y=220)
        messagebox.showinfo("Base Clientes", retorno)
        # Label(
        #        aplicacion, text="Registro No Eliminado", font="Courier, 15", fg="blue2"
        #    ).place(x=400, y=220)


    boton_borrar = Button(
    aplicacion,
    text="Eliminar",
    bg="Grey49",
    fg="white",
    padx=60,
    pady=3,
    command=lambda: aviso_borrar(tree),
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


    def aviso_modificar(
        valor_cuenta,
        valor_reparto,
        valor_cliente,
        valor_sucursal,
        valor_razon,
        valor_direccion,
        valor_localidad,
        tree,
        ):
        retorno = funcion_modificar(
        valor_cuenta,
        valor_reparto,
        valor_cliente,
        valor_sucursal,
        valor_razon,
        valor_direccion,
        valor_localidad,
        tree,
        )
        messagebox.showinfo("Base Clientes", retorno)


    boton_modificar = Button(
    aplicacion,
    text="Modificar",
    bg="Grey49",
    fg="white",
    padx=56,
    pady=3,
    command=lambda: aviso_modificar(
    valor_cuenta,
    valor_reparto,
    valor_cliente,
    valor_sucursal,
    valor_razon,
    valor_direccion,
    valor_localidad,
    tree,
    ),
    )
    boton_modificar.grid(row=5, column=2)
    boton_actualizar = Button(
    aplicacion,
    text="Actualizar",
    bg="Grey49",
    fg="white",
    padx=56,
    pady=3,
    command=lambda: funcion_actualizar(tree),
    )
    boton_actualizar.grid(row=6, column=2)


    boton_buscar = Button(
    aplicacion,
    text="Buscar",
    bg="Grey49",
    fg="white",
    command=lambda: funcion_buscar(valor_busqueda, tree),
    )
    boton_buscar.grid(row=9, column=0, padx=17, pady=8, ipady=1, ipadx=10, sticky="w")


    boton_imprimir = Button(
    aplicacion,
    text="Exportar Archivo",
    bg="Grey49",
    fg="white",
    padx=56,
    pady=3,
    command=lambda: funcion_imprimir(tree),
    )
    boton_imprimir.grid(row=4, column=3)


    #aplicacion.mainloop()
