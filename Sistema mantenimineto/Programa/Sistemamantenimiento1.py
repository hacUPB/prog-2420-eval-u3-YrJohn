#zona de diccionarios y conjuntos vacios
aviones = {}
tecnicos_disponibles = set()
tecnicos_ocupados = set()
tecnicos = {}


#Zona de funciones (def)
#se usa para registrar nuevos aviones en la "base de datos"
def registrar_avion(matricula, modelo, capacidad):
  
    #Uso esta parte para verificar si el avion ya esta dentro del diccionario de aviones
    if matricula in aviones:
        print(f"El avion con matricula {matricula} ya se encuentra en la base de datos")
        return
    
    #agrego el avion a la base
    aviones[matricula] = {
        "matricula": matricula,
        "modelo": modelo,
        "capacidad": capacidad,
        "estado": "operando", #Al inicio voy a suponer que el avion esta operando
        "historial": []
    }

    print(f"Avion con de # de matricula {matricula} registrado con exito")


#Se utiliza para registar los mantenimientos que se le vayan haciendo al avion
def registrar_mantenimiento(matricula, fecha, tipo, tecnico, observaciones=""):
    #primero se verifica si el avion existe
    if matricula not in aviones:
        print(f"El avion con matricula #{matricula} no se encuentra registrado en nuestras instalaciones" )
        return
    
    #se agrega el mantenimiento al avion
    nuevo_mantenimiento = {
        "fecha": fecha,
        "tipo": tipo,
        "tecnico": tecnico,
        "observaciones": observaciones
    }

    aviones[matricula] ["historial"].append (nuevo_mantenimiento)

#se usa para cambiar la operatividad del avion
    if tipo =="correctivo":
        aviones [matricula]["estado"] = "en mantenimiento"

    if tipo == "preventivo":
        aviones [matricula]["estado"] = "Operando"




    print(f"mantenimiento registrado con exito al avion con matricula numero {matricula}")


#este def lo uso para organizar los mantenimientos, ya que solo imprilos hace que se vea desorganizado
def ver_historial(matricula):
    #verifivo si el avion existe
    if matricula not in aviones:
        print(f"no hay ningun avion con el numero de matricula{matricula}")
        return
    
    historial= aviones[matricula]["historial"] #Saco el historial del avion a otra variable para poder utilizarlo mas facilmente

    if not historial: #si el avion no tienen mantemientos asciados se lo informo al usuario
        print(f"el avion {matricula} no tiene registros de mantenimiento asociados")
        return
    
    print(f"Historial de mantenimmiento para el avion {matricula}:")
    for i, mantenimiento in enumerate(historial, 1): #enumero los mantenimientos para asi poder mostrarlos de forma mucho mas organizada
        print(f"mantenimiento {i}:")
        print(f"{mantenimiento['fecha']}")
        print(f"{mantenimiento['tipo']}")
        print(f"{mantenimiento['tecnico']}")
        print(f"{mantenimiento['observaciones']}")

def estado_avion(matricula):
    #imprime el estado de la flota de aviones
    if matricula not in aviones:
        print(f"No se encontro ningun avion con matricula {matricula}")
        return
    
    estado = aviones[matricula]["estado"]

    print(f"El estado del avion con matricula{matricula} es {estado}")




def añadir_tecnico(nombre, especialidad):
        #añade los tecnicos a una lista
        if nombre in tecnicos:
            print(f"El tecnico {nombre} ya se encuentra registrado")
            return
        tecnicos_disponibles.add(nombre,)
        tecnicos[nombre] = {
            "especialidad": especialidad,
        }
       

        print(f"tecnico añadido exitosamente")


def eliminar_tecnico(nombre):
    if nombre in tecnicos:
        del tecnicos[nombre]
        tecnicos_disponibles.remove(nombre) #supondre que el tecnico al momento de eliminarlo no se encuentra realizando ningun trabajo
        print(f"Tecnico {nombre} eliminado exitosamente")
        return
    print(f"el tecnico {nombre} no se encuentra registrado")


def asignar_tecnico(nombre):
    if nombre in tecnicos_disponibles:
        tecnicos_disponibles.remove(nombre)
        tecnicos_ocupados.add(nombre) #primero elimino el tecnico de estar disponibl y lo coloco ocupado 
        print(f"el tecnico {nombre} ahora se encuentra ocupado")
    else:
        print(f"el tecnico {nombre} no se encuentra disponible para asignacion")

def desasignar_tecnico(nombre):
    if nombre in tecnicos_ocupados:
        tecnicos_ocupados.remove(nombre) #elimino el tecnico de estar ocupado a estar disponible
        tecnicos_disponibles.add(nombre)
        print(f"el tecnico {nombre} ahora se encuentra disponible")
    else: 
        print(f"el tecnico {nombre} no se encuentra ocupado")

def ver_tecnico(nombre):
    if nombre in tecnicos_disponibles:
        print(f"El tecnico {nombre} se encuentra disponible")
    elif nombre in tecnicos_ocupados:
        print(f"El tecnico se encuentra ocupado en el momento")
    else:
        print(f"el tecnico {nombre} no se encuentra registrado")


registrar_avion("B123", "BOEING 767", 180)
registrar_avion("B1234", "BOEING 767", 180)

registrar_mantenimiento("B123", "2024-10-24", "preventivo", "john", "revision usual")
registrar_mantenimiento("B123", "2025-10-94", "correctivo", "john", "revision")
registrar_mantenimiento("B123", "2024-10-24", "preventivo", "john", "revision usual")


estado_avion("B123")
ver_historial("B123")
añadir_tecnico("John", "Mecanico")




asignar_tecnico("John")
desasignar_tecnico("John")

eliminar_tecnico("John") 
print(aviones)
print(tecnicos)

print(tecnicos_disponibles)
print(tecnicos_ocupados)