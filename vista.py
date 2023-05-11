from tkinter import IntVar
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from tkinter import Tk
from modelo import operaciones


class Ventana:
    def __init__(self, ventana):
        self.objeto_uno = operaciones()
        self.aplicacion = ventana

        self.valor_cuenta = IntVar()
        self.valor_reparto = IntVar()
        self.valor_cliente = IntVar()
        self.valor_sucursal = IntVar()
        self.valor_razon = StringVar()
        self.valor_direccion = StringVar()
        self.valor_localidad = StringVar()
        self.valor_busqueda = StringVar()

        self.titulo = Label(
            self.aplicacion,
            text="BASE CLIENTES",
            bg="Grey49",
            fg="white",
            height=1,
            width=55,
            font=("bold"),
        )
        self.titulo.grid(
            row=0, column=0, columnspan=7, padx=1, pady=1, sticky="w" + "e"
        )

        self.cuenta = Label(
            self.aplicacion, text="Cuenta :", fg="black", anchor="center"
        )
        self.cuenta.grid(row=1, column=0, sticky="w")
        self.reparto = Label(
            self.aplicacion, text="Reparto :", fg="black", anchor="center"
        )
        self.reparto.grid(row=2, column=0, sticky="w")
        self.numero_de_cliente = Label(
            self.aplicacion,
            text="Numero de Cliente : ",
            fg="black",
            anchor="center",
        )
        self.numero_de_cliente.grid(row=3, column=0, sticky="w")
        self.sucursal = Label(
            self.aplicacion,
            text="Sucursal:",
            fg="black",
            anchor="center",
        )
        self.sucursal.grid(row=3, column=0, sticky="e")
        self.razonsocial = Label(
            self.aplicacion, text="Razon Social : ", fg="black", anchor="center"
        )
        self.razonsocial.grid(row=4, column=0, sticky="w")
        self.direccion = Label(
            self.aplicacion, text="Direccion : ", fg="black", anchor="center"
        )
        self.direccion.grid(row=5, column=0, sticky="w")
        self.localidad = Label(
            self.aplicacion, text="Localidad :", fg="black", anchor="center"
        )
        self.localidad.grid(row=6, column=0, sticky="w")

        self.entry_cuenta = Entry(
            self.aplicacion, textvariable=self.valor_cuenta, width=15
        )
        self.entry_cuenta.grid(row=1, column=0)
        self.entry_reparto = Entry(
            self.aplicacion, textvariable=self.valor_reparto, width=15
        )
        self.entry_reparto.grid(row=2, column=0)
        self.entry_numero_de_cliente = Entry(
            self.aplicacion, textvariable=self.valor_cliente, width=15
        )
        self.entry_numero_de_cliente.grid(row=3, column=0)
        self.entry_sucursal = Entry(
            self.aplicacion, textvariable=self.valor_sucursal, width=5
        )
        self.entry_sucursal.grid(row=3, column=1, sticky="w")
        self.entry_razonsocial = Entry(
            self.aplicacion, textvariable=self.valor_razon, width=30
        )
        self.entry_razonsocial.grid(row=4, column=0)
        self.entry_direccion = Entry(
            self.aplicacion, textvariable=self.valor_direccion, width=30
        )
        self.entry_direccion.grid(row=5, column=0)
        self.entry_localidad = Entry(
            self.aplicacion, textvariable=self.valor_localidad, width=30
        )
        self.entry_localidad.grid(row=6, column=0)
        self.entrybusqueda = ttk.Entry(
            self.aplicacion, textvariable=self.valor_busqueda
        )
        self.entrybusqueda.grid(row=9, column=0, padx=55, pady=8, ipady=3, ipadx=60)

        # -------------------------------------------------
        # TREEVIEW
        # -------------------------------------------------

        self.tree = ttk.Treeview(self.aplicacion)

        self.aplicacion.geometry("950x700")

        self.scroll = ttk.Scrollbar(self.aplicacion)
        self.scroll.place(x=920, y=270, height=420, width=25)
        self.tree.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tree.yview)

        self.s = ttk.Style()
        self.s.theme_use("clam")
        self.s.configure(
            "Treeview.Heading", background="Grey49", bg="white", fg="white"
        )
        self.s.configure(
            "Treeview",
            background="grey74",
            fieldbackground="grey74",
            foreground="black",
        )
        self.s.configure(
            "Vertical.TScrollbar",
            gripcount=6,
            background="White",
            darkcolor="Black",
            troughcolor="gray78",
            bordercolor="Black",
            arrowcolor="gray36",
        )

        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
        self.tree.column("#0", width=30, minwidth=80, anchor="center")
        self.tree.column("col1", width=40, minwidth=80, anchor="center")
        self.tree.column("col2", width=40, minwidth=80, anchor="center")
        self.tree.column("col3", width=70, minwidth=80, anchor="center")
        self.tree.column("col4", width=40, minwidth=80, anchor="center")
        self.tree.column("col5", width=200, minwidth=80, anchor="w")
        self.tree.column("col6", width=250, minwidth=80, anchor="w")
        self.tree.column("col7", width=250, minwidth=200, anchor="w")
        
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Cuenta")
        self.tree.heading("col2", text="Reparto")
        self.tree.heading("col3", text="Nº de Cliente")
        self.tree.heading("col4", text="Sucursal")
        self.tree.heading("col5", text="Razon Social")
        self.tree.heading("col6", text="Direccion")
        self.tree.heading("col7", text="Localidad")

        self.tree.bind("<<TreeviewSelect>>", self.seleccion, add=True)

        self.tree.grid(column=0, row=20, columnspan=5, ipady=100)
        self.boton_alta = Button(
            self.aplicacion,
            text="Alta",
            bg="Grey49",
            fg="white",
            padx=71,
            pady=3,
            command=lambda: self.aviso_alta(
                self.valor_cuenta,
                self.valor_reparto,
                self.valor_cliente,
                self.valor_sucursal,
                self.valor_razon,
                self.valor_direccion,
                self.valor_localidad,
                self.tree,
            ),
        )
        self.boton_alta.grid(row=3, column=2)
        self.boton_borrar = Button(
            self.aplicacion,
            text="Eliminar",
            bg="Grey49",
            fg="white",
            padx=60,
            pady=3,
            command=lambda: self.aviso_borrar(self.tree),
        )
        self.boton_borrar.grid(row=4, column=2)
        self.boton_salir = Button(
            self.aplicacion,
            text="Salir",
            bg="Grey49",
            fg="white",
            padx=60,
            pady=3,
            command=self.aplicacion.quit,
        )
        self.boton_salir.grid(row=7, column=3)
        self.boton_modificar = Button(
            self.aplicacion,
            text="Modificar",
            bg="Grey49",
            fg="white",
            padx=56,
            pady=3,
            command=lambda: self.aviso_modificar(
                self.valor_cuenta,
                self.valor_reparto,
                self.valor_cliente,
                self.valor_sucursal,
                self.valor_razon,
                self.valor_direccion,
                self.valor_localidad,
                self.tree,
            ),
        )

        self.boton_modificar.grid(row=5, column=2)
        
        self.boton_actualizar = Button(
            self.aplicacion,
            text="Actualizar",
            bg="Grey49",
            fg="white",
            padx=56,
            pady=3,
            command=lambda: self.objeto_uno.funcion_actualizar(self.tree),
        )
        self.boton_actualizar.grid(row=6, column=2)
        """
        self.boton_buscar = Button(
            self.aplicacion,
            text="Buscar",
            bg="Grey49",
            fg="white",
            command=lambda: self.objeto_uno.funcion_buscar(
                self.valor_busqueda, self.tree
            ),
        )
        self.boton_buscar.grid(
            row=9, column=0, padx=17, pady=8, ipady=1, ipadx=10, sticky="w"
        )

        self.boton_imprimir = Button(
            self.aplicacion,
            text="Exportar Archivo",
            bg="Grey49",
            fg="white",
            padx=56,
            pady=3,
            command=lambda: self.objeto_uno.funcion_imprimir(self.tree),
        )
        self.boton_imprimir.grid(row=4, column=3)
          """

    # METODOS-----------------------------------------------------------

    def aviso_alta(self, valor_cuenta, valor_reparto, valor_cliente, valor_sucursal, valor_razon, valor_direccion, valor_localidad, tree):
        retorno = self.objeto_uno.funcion_alta(
            self.valor_cuenta,
            self.valor_reparto,
            self.valor_cliente,
            self.valor_sucursal,
            self.valor_razon,
            self.valor_direccion,
            self.valor_localidad,
            tree,
        )
        if messagebox.showinfo("Base Clientes", retorno):
            Label(
                self.aplicacion, text="Registro valido", font="Courier, 10", fg="blue2"
            ).place(x=280, y=100)
        else:
            messagebox.showinfo("Base Clientes", retorno)

     
    def aviso_borrar(self, tree):
        retorno = self.objeto_uno.funcion_borrar(tree)
        # Label(
        # aplicacion, text="Registro Eliminado", font="Courier, 15", fg="blue2"
        # ).place(x=400, y=220)
        messagebox.showinfo("Base Clientes", retorno)
        # Label(
        #        aplicacion, text="Registro No Eliminado", font="Courier, 15", fg="blue2"
        #    ).place(x=400, y=220)

    def seleccion(self, a):
        self.valor_cuenta.set("")
        self.valor_reparto.set("")
        self.valor_cliente.set("")
        self.valor_sucursal.set("")
        self.valor_razon.set("")
        self.valor_direccion.set("")
        self.valor_localidad.set("")
        dato = self.tree.focus()
        item = dict(self.tree.item(dato))
        #try:
        self.valor_cuenta.set(item.get("values")[0])
        self.valor_reparto.set(item.get("values")[0])
        self.valor_cliente.set(item.get("values")[1])
        self.valor_sucursal.set(item.get("values")[2])
        self.valor_razon.set(item.get("values")[3])
        self.valor_direccion.set(item.get("values")[4])
        self.valor_localidad.set(item.get("values")[5])
        #except:
        #    pass

    def aviso_modificar(
        self,
        valor_cuenta,
        valor_reparto,
        valor_cliente,
        valor_sucursal,
        valor_razon,
        valor_direccion,
        valor_localidad,
        tree,
    ):
        retorno = self.objeto_uno.funcion_modificar(
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
      

        
    def actualizar(
        self,
    ):
        self.objeto_uno.funcion_actualizar(self.tree)

"""
if __name__ == "__main__":

    app = Tk()
    objeto1 = Ventana(app)
    app.mainloop()
"""