import tkinter as tk
from vista.vista import Frame
from include.menu import barrita_menu
from modelo.consultas_dao import crear_tabla

def main():
    crear_tabla()

    ventana=tk.Tk()
    ventana.title("Locales en Altos de Podestá")
    icono=tk.PhotoImage(file="img/local.png")
    ventana.iconphoto(False, icono)
    ventana.resizable(0,0)

    barrita_menu(ventana)
    app=Frame(root=ventana)

    ventana.mainloop()

if __name__ == "__main__":
    main()
