import sqlite3
import re
import csv
import os

my_data = (
    []
)  # variable global que me permite en la funcion_imprimir(), pasar el string de datos del treeview


def base():
    con = sqlite3.connect("base_ejemplo.db")
    return con


def crear_tabla():
    con = base()
    cursor = con.cursor()
    sql = "CREATE TABLE clientes (cuenta INTERGER, reparto INTERGER, numero_de_cliente INTERGER PRIMARY KEY, sucursal INTERGER, razonsocial VARCHAR, direccion VARCHAR, localidad VARCHAR)"
    cursor.execute(sql)
    con.commit()


try:
    base()
    crear_tabla()
except:
    print("Hay un error")

# Funciones CRUD-------------------------------------------------------------------------


def actualizar(tree):

    records = tree.get_children()
    global my_data
    for element in records:
        tree.delete(element)
    sql = "SELECT * FROM clientes ORDER BY cuenta ASC"
    con = base()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    my_data = datos.fetchall()
    for fila in my_data:
        print(fila)
        tree.insert(
            "",
            "end",
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]),
        )


# ----------------------------------------------------------------------------------------


def funcion_alta(
    cuenta,
    reparto,
    numero_de_cliente,
    sucursal,
    razonsocial,
    direccion,
    localidad,
    tree,
):

    regex = razonsocial.get()
    expresion = "[a-zA-ZÀ-ÿ(0-9)]"
    if re.match(expresion, regex):
        # Label(
        #    aplicacion, text="Registro valido", font="Courier, 10", fg="blue2"
        # ).place(x=280, y=100)
        con = base()
        cursor = con.cursor()
        data = (
            cuenta.get(),
            reparto.get(),
            numero_de_cliente.get(),
            sucursal.get(),
            razonsocial.get(),
            direccion.get(),
            localidad.get(),
        )
        sql = "INSERT INTO clientes(cuenta, reparto, numero_de_cliente, sucursal, razonsocial, direccion, localidad) VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        actualizar(tree)
        cuenta.set(""), reparto.set(""), numero_de_cliente.set(""), sucursal.set(
            ""
        ), razonsocial.set(""), direccion.set(""), localidad.set("")
        return "Registro dado de alta"
    else:
        return ("Error", "No se creo el registro")


# -----------------------------------------------------------------------------------------------------------


def funcion_borrar(tree):
    cliente = tree.selection()
    item = tree.item(cliente)
    print(item)
    print(item["text"])
    mi_id = item["text"]
    con = base()
    cursor = con.cursor()
    data = (mi_id,)
    tree.delete(cliente)
    sql = "DELETE FROM clientes WHERE cuenta = ?;"
    cursor.execute(sql, data)
    con.commit()

    return "Registro eliminado"


# ------------------------------------------------------------------------------------------------------------


def funcion_modificar(
    cuenta,
    reparto,
    numero_de_cliente,
    sucursal,
    razonsocial,
    direccion,
    localidad,
    tree,
):
    cliente = tree.selection()
    item = tree.item(cliente)
    mi_id = item["text"]
    con = base()
    cursor = con.cursor()
    sql = f"UPDATE clientes SET cuenta = '{cuenta.get()}', reparto = '{reparto.get()}', numero_de_cliente = '{numero_de_cliente.get()}', sucursal = '{sucursal.get()}', razonsocial = '{razonsocial.get()}', direccion = '{direccion.get()}', localidad = '{localidad.get()}' WHERE cuenta = '{mi_id}';"
    cursor.execute(sql)
    con.commit()
    actualizar(tree)
    cuenta.set(""), reparto.set(""), numero_de_cliente.set(""), sucursal.set(
        ""
    ), razonsocial.set(""), direccion.set(""), localidad.set("")
    return "Registro modificado"


# -----------------------------------------------------------------------------------------------------------


def funcion_buscar(busqueda, tree):
    records = tree.get_children()
    global my_data
    for element in records:
        tree.delete(element)
    sql = f"SELECT * FROM clientes WHERE cuenta LIKE '%{busqueda.get()}%' OR reparto LIKE '%{busqueda.get()}%' OR numero_de_cliente LIKE '%{busqueda.get()}%' OR sucursal LIKE '%{busqueda.get()}%' OR razonsocial LIKE '%{busqueda.get()}%' OR direccion LIKE '%{busqueda.get()}%' OR localidad LIKE '%{busqueda.get()}%' "
    con = base()
    cursor = con.cursor()
    datos = cursor.execute(sql)
    my_data = datos.fetchall()
    for fila in my_data:
        print(fila)
        tree.insert(
            "",
            "end",
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]),
        )


def funcion_imprimir(tree):
    # codigo para generar un txt con resultado del treeview -------
    with open("pendientes.txt", "w") as f:
        for item_id in tree.get_children():
            item = tree.item(item_id)
    print(item["text"], item["values"], file=f)

    # genera archivo CSV----------------------------------------------
    """
    if len(my_data) < 1:
        #showwarning("Base Clientes", "El archivo no fue exportado")
        return False
    fln = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Archivo CSV",
        filetypes=(("CVS Archivo", ".csv"), ("All files", ".*")),
    )
    with open(fln, mode="w") as myfile:
        exp_writer = csv.writer(myfile, delimiter=",")
        for i in my_data:
            exp_writer.writerow(i)
    messagebox.showinfo(
        "Archivo Exportado",
        "El archivo " + os.path.basename(fln) + " se exporto correctamente.",
    )"""
