from .consultas_dao import listar_regiones

class RegionManager:
    def __init__(self):
        self.regiones=[]
        self.cargar_regiones()
    
    def cargar_regiones(self):
        y=listar_regiones()
        self.regiones = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
        for region in y:
            self.regiones.append({'id': region[0], 'Nombre': region[1]})
    
    def get_nombres_r(self):
        return [region['Nombre'] for region in self.regiones]
    
    def get_id_por_indice_r(self, index):
        if 0 <= index < len(self.regiones):
            return self.regiones[index]['id']
        return None
    
    def get_id_por_nombre_r(self, nombre):
        for region in self.regiones:
            if region['Nombre'] == nombre:
                return region['id']
        return None
    
    def get_indice_por_nombre_r(self, nombre):
        for i, region in enumerate(self.regiones):
            if region['Nombre'] == nombre:
                return i
        return 0

