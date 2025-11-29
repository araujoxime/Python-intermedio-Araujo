from .consultas_dao import listar_categorias

class CategoriaManager:
    def __init__(self):
        self.categorias=[]
        self.cargar_categorias()
    
    def cargar_categorias(self):
        x=listar_categorias()
        self.categorias = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
        for categoria in x:
            self.categorias.append({'id': categoria[0], 'Nombre': categoria[1]})
    
    def get_nombres_c(self):
        return [categoria['Nombre'] for categoria in self.categorias]
    
    def get_id_por_indice_c(self, index):
        if 0 <= index < len(self.categorias):
            return self.categorias[index]['id']
        return None
    
    def get_id_por_nombre_c(self, nombre):
        for categoria in self.categorias:
            if categoria['Nombre'] == nombre:
                return categoria['id']
        return None
    
    def get_indice_por_nombre_c(self, nombre):
        for i, categoria in enumerate(self.categorias):
            if categoria['Nombre'] == nombre:
                return i
        return 0

