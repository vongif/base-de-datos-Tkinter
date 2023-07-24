import sqlite3
import re
from peewee import *
from types import MethodType

from decoradores import decorador_alta
from decoradores import decorador_eliminar
from decoradores import decorador_actualizar
from observador import Sujeto


# import csv
# import os


# BASE DE DATOS---------------------------------------------------------------

db = SqliteDatabase("base_ejemplo.db")


class BaseModel(Model):
    class Meta:
        database = db


class Clientes(BaseModel):
    cuenta = IntegerField()
    reparto = IntegerField()
    numero_de_cliente = IntegerField()
    sucursal = IntegerField()
    razonsocial = CharField()
    direccion = CharField()
    localidad = CharField()


db.connect()
db.create_tables([Clientes])


# CRUD---------------------------------------------------------------


class operaciones(Sujeto):
    def __init__(self):
        pass

    # Funciones CRUD-------------------------------------------------------------------------
    @decorador_alta
    def funcion_alta(
        self,
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

            clientes = Clientes()
            clientes.cuenta = cuenta.get()
            clientes.reparto = reparto.get()
            clientes.numero_de_cliente = numero_de_cliente.get()
            clientes.sucursal = sucursal.get()
            clientes.razonsocial = razonsocial.get()
            clientes.direccion = direccion.get()
            clientes.localidad = localidad.get()
            clientes.save()
            self.funcion_actualizar(tree)
            self.notificar(
                clientes.cuenta,
                clientes.reparto,
                clientes.numero_de_cliente,
                clientes.razonsocial,
            )
            cuenta.set(""), reparto.set(""), numero_de_cliente.set(""), sucursal.set(
                ""
            ), razonsocial.set(""), direccion.set(""), localidad.set("")
            return (
                "Registro dado de alta: ",
                "\n", "Cuenta: ",
                clientes.cuenta,
                "\n", "Reparto: ",
                clientes.reparto,
                "\n", "Numero de CLiente: ",
                clientes.numero_de_cliente,
                "\n", "Sucursal: ",
                clientes.sucursal,
                "\n", "Razon Social: ",
                clientes.razonsocial,
                "\n", "Direccion: ",
                clientes.direccion,
                "\n", "Localidad",
                clientes.localidad,
            )
        else:
            return ("Error", "No se creo el registro")

    @decorador_actualizar
    def funcion_actualizar(self, tree):

        records = tree.get_children()
        global my_data
        for element in records:
            tree.delete(element)

        for fila in Clientes.select():
            tree.insert(
                "",
                "end",
                text=fila.id,
                values=(
                    fila.cuenta,
                    fila.reparto,
                    fila.numero_de_cliente,
                    fila.sucursal,
                    fila.razonsocial,
                    fila.direccion,
                    fila.localidad,
                ),
            )
        return (
            "Registro actualizado",
            "\n",
            "Cuenta: ",
            fila.cuenta,
            "\n",
            "Reparto: ",
            fila.reparto,
            "\n",
            "Numero de CLiente: ",
            fila.numero_de_cliente,
            "\n",
            "Sucursal: ",
            fila.sucursal,
            "\n",
            "Razon Social: ",
            fila.razonsocial,
            "\n",
            "Direccion: ",
            fila.direccion,
            "\n",
            "Localidad",
            fila.localidad,
        )

    # ----------------------------------------------------------------------------------------

    @decorador_eliminar
    def funcion_borrar(self, tree):
        cliente = tree.selection()
        item = tree.item(cliente)
        mi_id = item["text"]
        borrar = Clientes.get(Clientes.id == mi_id)
        borrar.delete_instance()
        print(borrar)
        self.funcion_actualizar(tree)
        return (
            "Registro eliminado: ",
            "\n",
            "Cuenta: ",
            item.get("values")[0],
            "\n",
            "Reparto: ",
            item.get("values")[1],
            "\n",
            "Numero de cliente: ",
            item.get("values")[2],
            "\n",
            "Sucursal: ",
            item.get("values")[3],
            "\n",
            "Razon Social: ",
            item.get("values")[4],
            "\n",
            "Direccion: ",
            item.get("values")[5],
            "\n",
            "Localidad: ",
            item.get("values")[6],
        )

    # ------------------------------------------------------------------------------------------------------------

    def funcion_modificar(
        self,
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
        actualizar = Clientes.update(
            cuenta=cuenta.get(),
            reparto=reparto.get(),
            numero_de_cliente=numero_de_cliente.get(),
            sucursal=sucursal.get(),
            razonsocial=razonsocial.get(),
            direccion=direccion.get(),
            localidad=localidad.get(),
        ).where(Clientes.id == mi_id)
        actualizar.execute()
        self.funcion_actualizar(tree)
        cuenta.set(""), reparto.set(""), numero_de_cliente.set(""), sucursal.set(
            ""
        ), razonsocial.set(""), direccion.set(""), localidad.set("")
        return "Registro modificado"

    # -----------------------------------------------------------------------------------------------------------

    def funcion_buscar(
        self,
        tree,
        busqueda,
    ):

        busqueda = busqueda.get()
        records = tree.get_children()
        global my_data
        for element in records:
            tree.delete(element)
            buscar = (
                Clientes.select().where(Clientes.id.contains(busqueda))
                | Clientes.select().where(Clientes.cuenta.contains(busqueda))
                | Clientes.select().where(Clientes.reparto.contains(busqueda))
                | Clientes.select().where(Clientes.numero_de_cliente.contains(busqueda))
                | Clientes.select().where(Clientes.sucursal.contains(busqueda))
                | Clientes.select().where(Clientes.razonsocial.contains(busqueda))
                | Clientes.select().where(Clientes.direccion.contains(busqueda))
                | Clientes.select().where(Clientes.localidad.contains(busqueda))
            )
            buscar.execute()
        try:
            for fila in buscar:
                tree.insert(
                    "",
                    "end",
                    text=fila.id,
                    values=(
                        fila.cuenta,
                        fila.reparto,
                        fila.numero_de_cliente,
                        fila.sucursal,
                        fila.razonsocial,
                        fila.direccion,
                        fila.localidad,
                    ),
                )
        except:
            print(f"No se enontro ningun registro con la busqueda: '{busqueda}'")
        else:
            print(
                f"El resultado es :  ID={fila.id}, Cuenta={fila.cuenta}, Reparto={fila.reparto}, Razon Social={fila.razonsocial}"
            )
