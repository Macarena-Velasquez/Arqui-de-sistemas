import psycopg2

conec = None
cur = None

def conexion():
    try:
        global conec
        global cur
        conec = psycopg2.connect(host="localhost", database="arqui", port='5432', user="postgres", password="hola1234")
        print("Conexión con base de datos establecida")
        cur = conec.cursor()
    except:
        print("Error de conexión con base de datos")

    
def consultar(sqlquery):
    cur.execute(sqlquery)
    return cur.fetchall()

def modificar(sqlquery):
    cur.execute(sqlquery) 
    conec.commit()  

def cerrar():
    try:
        cur.close()
        conec.close()
        print("Conexión con base de datos cerrada")
    except:
        print("Error al cerrar conexión")    


def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux


conexion()
#y = modificar("insert into funcionarios(especialidad, rut, nombre) values('Enfermero', '196443732', 'cristobal-urrutia')")
#modificar("update funcionarios set rut = '123456789' where nombre = 'cristobal-castro'")
print("consulta")

#y = modificar("insert into perros(nombre, edad, raza, descripcion) values('{data[3]}','{data[2]}', '{data[1]}','{data[0]}')")
#x = consultar("SELECT idmascota FROM mascota where nombre='eli';")

#print(x[0])
