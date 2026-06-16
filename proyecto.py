import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt


'''st.title("Proyecto Grupal de programacion")
st.write("Empecemos a trabajar equipo!")'''


#lectura del dataset
#escuelas = []
#with open("establecimientos-educativos-12K.csv", newline='') as escuelas_ba:
#    lector = csv.reader(escuelas_ba)
#
#   for escuela in lector:
#      escuelas.append(escuela)

with open('establecimientos-educativos-prueba.csv', encoding="utf-8") as escuelas_ba:
    escuelas_ba = csv.reader(escuelas_ba)

    municipio_id=[]
    municipio_nombre=[]
    establecimiento_id=[]
    establecimiento_nombre=[]
    modalidad=[]
    nivel=[]
    direccion=[]
    telefono=[]
    email=[]
    sector=[]
    tipo_organizacion=[]
    ambito=[]
    matricula=[]
    matricula_varones=[]
    matricula_mujeres=[]
    turnos=[]
   
    for escuela in escuelas_ba:
        municipio_id.append(escuela[0])	
        municipio_nombre.append(escuela[1])
        establecimiento_id.append(escuela[2])
        establecimiento_nombre.append(escuela[3])
        modalidad.append(escuela[8])
        nivel.append(escuela[9])
        direccion.append(escuela[10])
        telefono.append(escuela[11])
        email.append(escuela[12])
        sector.append(escuela[13])
        tipo_organizacion.append(escuela[15])
        ambito.append(escuela[17])
        matricula.append(escuela[25])
        matricula_varones.append(escuela[26])
        matricula_mujeres.append(escuela[27])
        turnos.append(escuela[29])
        
    diccionario={municipio_id[0]:municipio_id[1:],
                 municipio_nombre[0]:municipio_nombre[1:],
                 establecimiento_id[0]:establecimiento_id[1:],
                 establecimiento_nombre[0]:establecimiento_nombre[1:],
                 modalidad[0]:modalidad[1:],
                 nivel[0]:nivel[1:],
                 direccion[0]:direccion[1:],
                 telefono[0]:telefono[1:],
                 email[0]:email[1:],
                 sector[0]:sector[1:],
                 tipo_organizacion[0]:tipo_organizacion[1:],
                 ambito[0]:ambito[1:],
                 matricula[0]:matricula[1:],
                 matricula_varones[0]:matricula_varones[1:],
                 matricula_mujeres[0]:matricula_mujeres[1:],
                 turnos[0]:turnos[1:]}
    
def cantidad_valores(clave:str)->int:
    "Toma una clave del diccionario y evalua cuántos elementos posee la lista que representa su valor."
    tamaño = 0
    for i in diccionario[clave]:
        tamaño+=1
    return tamaño

print(cantidad_valores("nivel"))

def tipos_valores(clave:str) -> list:
    tipos_valores=[]
    for i in diccionario[clave]:
        if i not in tipos_valores:
            tipos_valores.append(i)
    return tipos_valores

print(tipos_valores("modalidad"))

def niveles(nivel: str, modalidad:str) -> list:
    """  Filtra y devuelve una lista con todas las escuelas que pertenecen 
    al nivel educativo dado.

    niveles("Primario") = 
    niveles("Secundario") = 
    niveles("Inicial") = Hoja de cálculo sin título - 
    """
    list_nivel = []

    for i in range (0,cantidad_valores("nivel")):
        if diccionario["nivel"][i] == nivel and diccionario["modalidad"][i] == modalidad:
            list_nivel.append(diccionario["establecimiento_nombre"][i])
    return list_nivel

#print(niveles('Nivel Secundario'))

#def suma(lista: list, sexo: int) -> int:
#    """ Calcula el total de alumnos de un sexo específico 
#    sumando los datos de la lista de escuelas.

#    suma([['Escuela     ]], ) = 10
#    suma([['Escuela' ], ['Escuela' ,  ]],  ) = 
#    suma([], ) = 0
#    """
#    total = 0

#    for escuela in lista:
#        total = total + int(escuela[sexo])
#    return total



def cantidad(nivel: str, sexo: int) -> int:
    """  Calcula la cantidad total de alumnos de un sexo determinado en un 
    nivel educativo específico.
cantidad("Inicial",             ) = 
cantidad("Primario",       ) = 
cantidad("Secundario",  ) = 
    """
    for i in tipos_niveles():
        return suma(niveles(i), sexo) 

VARONES = diccionario["matricula_varones"]
MUJERES = diccionario["matricula_mujeres"]

print("Varones primaria:", cantidad("Nivel Primario", VARONES))
print("Mujeres primaria:", cantidad("Nivel Primario", MUJERES))

print("Varones secundaria:", cantidad("Nivel Secundario", VARONES))
print("Mujeres secundaria:", cantidad("Nivel Secundario", MUJERES))

print("Varones inicial:", cantidad("Nivel Inicial", VARONES))
print("Mujeres inicial:", cantidad("Nivel Inicial", MUJERES))



