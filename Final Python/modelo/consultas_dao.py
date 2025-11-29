from .coneciondb import Coneccion

def crear_tabla():
    conn = Coneccion()

    sql= '''
        CREATE TABLE IF NOT EXISTS Categoria(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(50) UNIQUE
        );

        CREATE TABLE IF NOT EXISTS Region(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(50) UNIQUE
        );

    CREATE TABLE IF NOT EXISTS Locales(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(150),
            Manzana VARCHAR(10),
            Casa VARCHAR(10),
            Telefono VARCHAR(20),
            Categoria INTEGER,
            Region INTEGER,
            FOREIGN KEY (Categoria) REFERENCES Categoria(ID),
            FOREIGN KEY (Region) REFERENCES Region(ID)
            );
    '''
    try:
        conn.cursor.executescript(sql)
        
        categorias=['Almacén', 'Panaderia', 'Pizzeria', 'Kiosco', 'Verduleria', 'Carniceria', 'Dietetica']
        for nombre in categorias:
            conn.cursor.execute("INSERT OR IGNORE INTO Categoria (Nombre) VALUES (?);", (nombre,))
        
        regiones=['Entrada', 'Plaza principal', 'Plaza fondo', 'Plaza centro']
        for nombre in regiones:
            conn.cursor.execute("INSERT OR IGNORE INTO Region (Nombre) VALUES (?);", (nombre,))

        conn.conexion.commit()
        conn.cerrar_con()
    except:
        pass

class Locales():
    def __init__(self, nombre, categoria, region, manzana, casa, telefono):
        self.id_locales=None
        self.nombre=nombre
        self.categoria=categoria
        self.region=region
        self.manzana=manzana
        self.casa=casa
        self.telefono=telefono
    
    def __str__(self):
        return f'Local [{self.nombre}, {self.categoria}, {self.region}, {self.manzana}, {self.casa}, {self.telefono}]'

def guardar_local(local):
    conn=Coneccion()

    sql=f'''
        INSERT INTO Locales(Nombre, Categoria, Region, Manzana, Casa, Telefono)
        VALUES('{local.nombre}', '{local.categoria}', '{local.region}', '{local.manzana}', '{local.casa}', '{local.telefono}');
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def listar_local(condicion='todas', region='todas'):
    conn=Coneccion()
    listar_locales=[]
    sql=f'''
        SELECT l.ID, l.Nombre, c.Nombre as Categoria, r.Nombre as Region, l.Manzana, l.Casa, l.Telefono FROM Locales as l
        INNER JOIN Categoria as c
        ON l.Categoria=c.ID
        INNER JOIN Region as r
        ON l.Region=r.ID;
    '''
    condiciones=[]
    if condicion !='todas':
        condiciones.append(f"c.ID={condicion}")
    if region != 'todas':
        condiciones.append(f"r.ID={region}")
    if condiciones:
        sql+= " WHERE " + " AND ".join(condiciones)

    try:
        conn.cursor.execute(sql)
        listar_locales=conn.cursor.fetchall()
        conn.cerrar_con()
        return listar_locales
    except:
        pass

def listar_categorias():
    conn=Coneccion()
    sql='SELECT id, nombre FROM Categoria ORDER BY nombre;'

    try:
        conn.cursor.execute(sql)
        resultados=conn.cursor.fetchall()
        conn.cerrar_con()

        return resultados
    except Exception as e:
        print(f"Error al listar categorias: {e}")
        return ()
    finally:
        if not conn:
            conn.cerrar_con()

def listar_regiones():
    conn=Coneccion()
    sql='SELECT id, nombre FROM Region ORDER BY nombre;'

    try:
        conn.cursor.execute(sql)
        resultados=conn.cursor.fetchall()
        conn.cerrar_con()

        return resultados
    except Exception as e:
        print(f"Error al listar Regiones: {e}")
        return ()
    finally:
        if not conn:
            conn.cerrar_con()

def editar_local(local, id):
    conn=Coneccion()
    sql=f'''
       UPDATE Locales
       SET Nombre='{local.nombre}', Categoria='{local.categoria}', Region='{local.region}', Manzana='{local.manzana}', Casa='{local.casa}', Telefono='{local.telefono}'
       WHERE ID={id}
       ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def borrar_local(id):
    conn=Coneccion()
    sql=f'''
        DELETE FROM Locales
        WHERE ID={id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass