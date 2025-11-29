import tkinter as tk
from tkinter import ttk, messagebox
import modelo.consultas_dao as consulta
import modelo.categoria_dao as categoria
import modelo.region_dao as region

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root=root
        self.pack()
        self.fondo="#F3F861"
        self.config(bg=self.fondo)
        self.id_local=None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()
    
    def label_form(self):
        self.label_nombre=tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)
        
        self.label_nombre=tk.Label(self, text="Categoria: ")
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")    
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)
        
        self.label_nombre=tk.Label(self, text="Región: ")
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")    
        self.label_nombre.grid(row= 2, column=0,padx=10,pady=10)
        
        self.label_nombre=tk.Label(self, text="Manzana: ")
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")
        self.label_nombre.grid(row= 3, column=0,padx=10,pady=10)
        
        self.label_nombre=tk.Label(self, text="Casa: ")
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")
        self.label_nombre.grid(row= 4, column=0,padx=10,pady=10)
        
        self.label_nombre=tk.Label(self, text="Teléfono: ")
        self.label_nombre.config(font=('Arial',12,'bold'),bg="#FBFCDD",fg="#1931E8")
        self.label_nombre.grid(row= 5, column=0,padx=10,pady=10)
    
    def input_form(self):
        self.nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50, state="disabled")
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.categoria_manager=categoria.CategoriaManager()
        self.entry_categoria=ttk.Combobox(self, state="readonly")
        self.entry_categoria.config(width=50, state="disabled")
        self.entry_categoria['values']=self.categoria_manager.get_nombres_c()
        self.entry_categoria.current(0)

        def on_categoria_selected(event):
            selected_index=self.entry_categoria.current()
            categoria_id=self.categoria_manager.get_id_por_indice_c(selected_index)
            return categoria_id

        self.entry_categoria.bind("<<ComboboxSelected>>", on_categoria_selected)
        self.entry_categoria.grid(row=1, column=1, padx=10, pady=10)

        self.region_manager=region.RegionManager()
        self.entry_region=ttk.Combobox(self, state="readonly")
        self.entry_region.config(width=50, state="disabled")
        self.entry_region['values']=self.region_manager.get_nombres_r()
        self.entry_region.current(0)

        def on_region_selected(event):
            selected_index_r=self.entry_region.current()
            region_id=self.region_manager.get_id_por_indice_r(selected_index_r)
            return region_id

        self.entry_region.bind("<<ComboboxSelected>>", on_region_selected)
        self.entry_region.grid(row=2, column=1, padx=10, pady=10)

        self.manzana=tk.StringVar()
        self.entry_manzana=tk.Entry(self, textvariable=self.manzana)
        self.entry_manzana.config(width=50, state="disabled")
        self.entry_manzana.grid(row=3, column=1, padx=10, pady=10)

        self.casa=tk.StringVar()
        self.entry_casa=tk.Entry(self, textvariable=self.casa)
        self.entry_casa.config(width=50, state="disabled")
        self.entry_casa.grid(row=4, column=1, padx=10, pady=10)

        self.telefono=tk.StringVar()
        self.entry_telefono=tk.Entry(self, textvariable=self.telefono)
        self.entry_telefono.config(width=50, state="disabled")
        self.entry_telefono.grid(row=5, column=1, padx=10, pady=10)
    
    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)    
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_alta.grid(row= 6, column=0,padx=10,pady=10)   

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)    
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000', state='disabled')    
        self.btn_modi.grid(row= 6, column=1,padx=10,pady=10) 

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)    
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000', state='disabled')    
        self.btn_cance.grid(row= 6, column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')    
        self.entry_categoria.config(state='normal')    
        self.entry_region.config(state='normal')
        self.entry_manzana.config(state='normal') 
        self.entry_casa.config(state='normal')   
        self.entry_telefono.config(state='normal')
        self.btn_modi.config(state='normal')    
        self.btn_cance.config(state='normal')    
        self.btn_alta.config(state='disabled')
        self.entry_categoria.config(state="readonly")
        self.entry_region.config(state="readonly")
    
    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_categoria.config(state='disabled')    
        self.entry_region.config(state='disabled') 
        self.entry_manzana.config(state='disabled')
        self.entry_casa.config(state='disabled')    
        self.entry_telefono.config(state='disabled')    
        self.btn_modi.config(state='disabled')    
        self.btn_cance.config(state='disabled')    
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.manzana.set('')
        self.casa.set('')
        self.telefono.set('')
        self.entry_categoria.current(0)
        self.entry_categoria.config(state="disabled")
        self.entry_region.current(0)
        self.entry_region.config(state="disabled")
        self.id_local=None
    
    def mostrar_tabla(self):

        self.lista_l = consulta.listar_local()

        self.lista_l.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre','Categoria','Región', 'Manzana', 'Casa', 'Teléfono'))
        self.tabla.grid(row=7, column=0, columnspan=4, sticky='nse')
        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=7,column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Categoria')
        self.tabla.heading('#3', text='Región')
        self.tabla.heading('#4', text='Manzana')
        self.tabla.heading('#5', text='Casa')
        self.tabla.heading('#6', text='Teléfono')

        
        for l in self.lista_l:
            self.tabla.insert('',0,text=l[0],
                              values=(l[1],l[2],l[3],l[4],l[5],l[6]))
        
        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)    
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_editar.grid(row= 8, column=0,padx=10,pady=10)    

        self.btn_delete = tk.Button(self, text='Eliminar', command= self.eliminar_registro)    
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_delete.grid(row= 8, column=1,padx=10,pady=10)
    
    def guardar_campos(self):
        local=consulta.Locales(self.nombre.get(),
                               self.categoria_manager.get_id_por_indice_c(self.entry_categoria.current()),
                               self.region_manager.get_id_por_indice_r(self.entry_region.current()),
                               self.manzana.get(),
                               self.casa.get(),
                               self.telefono.get()
        )
        
        if self.id_local==None:
            consulta.guardar_local(local)
        else:
            consulta.editar_local(local, int(self.id_local))

        self.mostrar_tabla()
        self.bloquear_campos()
    
    def editar_registro (self):
        try:
            self.id_local=self.tabla.item(self.tabla.selection())['text']
            self.nombre_loc=self.tabla.item(self.tabla.selection())['values'][0]
            self.cat_loc=self.tabla.item(self.tabla.selection())['values'][1]
            self.reg_loc=self.tabla.item(self.tabla.selection())['values'][2]
            self.mza_loc=self.tabla.item(self.tabla.selection())['values'][3]
            self.cas_loc=self.tabla.item(self.tabla.selection())['values'][4]
            self.tel_loc=self.tabla.item(self.tabla.selection())['values'][5]

            self.habilitar_campos()
            self.nombre.set(self.nombre_loc)
            indice_categoria=self.categoria_manager.get_id_por_nombre_c(self.cat_loc)
            self.entry_categoria.current(indice_categoria)
            indice_region=self.region_manager.get_id_por_nombre_r(self.reg_loc)
            self.entry_region.current(indice_region)
            self.manzana.set(self.mza_loc)
            self.casa.set(self.cas_loc)
            self.telefono.set(self.tel_loc)
        except:
            pass
    
    def eliminar_registro(self):
        self.id_local=self.tabla.item(self.tabla.selection())['text']
        response=messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el registro?")
        if response:
            consulta.borrar_local(int(self.id_local))
        else:
            messagebox.showinfo("Atención", "El registro se conservara")
        self.id_local=None
        self.mostrar_tabla()
