import tkinter as tk
from modelo.consultas_dao import crear_tabla

def barrita_menu(root):
    barra=tk.Menu(root)
    root.config(menu=barra, width=300, height=300)
    menu_inicio=tk.Menu(barra, tearoff=0)
    menu_consultas=tk.Menu(barra, tearoff=0)

    #niveles
    barra.add_cascade(label="Inicio", menu=menu_inicio)
    barra.add_cascade(label="Consultas", menu=menu_consultas)
    barra.add_cascade(label="Acerca de...", menu=menu_inicio)
    barra.add_cascade(label="Ayuda", menu=menu_inicio)

    #Submenu inicio
    menu_inicio.add_command(label="Conectar DB", command=lambda: crear_tabla())
    menu_inicio.add_command(label="Desconectar DB")
    menu_inicio.add_command(label="Salir", command=root.destroy)

    #Submenu consultas
    menu_consultas.add_cascade(label="Agregar")
    menu_consultas.add_cascade(label="Modificar")
    menu_consultas.add_cascade(label="Eliminar")


