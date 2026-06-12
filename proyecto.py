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

with open('establecimientos-educativos-12K.csv', encoding="utf-8") as escuelas_ba:
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
        
    diccionario={municipio_id[0]:municipio_id,
                 municipio_nombre[0]:municipio_nombre,
                 establecimiento_id[0]:establecimiento_id,
                 establecimiento_nombre[0]:establecimiento_nombre,
                 modalidad[0]:modalidad,
                 nivel[0]:nivel,
                 direccion[0]:direccion,
                 telefono[0]:telefono,
                 email[0]:email,
                 sector[0]:sector,
                 tipo_organizacion[0]:tipo_organizacion,
                 ambito[0]:ambito,
                 matricula[0]:matricula,
                 matricula_varones[0]:matricula_varones,
                 matricula_mujeres[0]:matricula_mujeres,
                 turnos[0]:turnos}
    print(diccionario)
 


 

def niveles(nivel: str) -> list:
    """  Filtra y devuelve una lista con todas las escuelas que pertenecen 
    al nivel educativo dado.

    niveles("Primario") = 
    niveles("Secundario") = 
    niveles("Inicial") = 
    """
    list_nivel = []

    for escuela in escuelas:
        if escuela[8] == nivel:
            list_nivel.append(escuela)
    return list_nivel

def suma(lista: list, sexo: int) -> int:
    """ Calcula el total de alumnos de un sexo específico 
    sumando los datos de la lista de escuelas.

    suma([['Escuela     ]], ) = 10
    suma([['Escuela' ], ['Escuela' ,  ]],  ) = 
    suma([], ) = 0
    """
    total = 0

    for escuela in lista:
        total = total + int(escuela[sexo])
    return total

def cantidad(nivel: str, sexo: int) -> int:
    """  Calcula la cantidad total de alumnos de un sexo determinado en un 
    nivel educativo específico.
cantidad("Inicial",             ) = 
cantidad("Primario",       ) = 
cantidad("Secundario",  ) = 
    """
    return suma(niveles(nivel), sexo) 

VARONES = 26
MUJERES = 27

#print("Varones primaria:", cantidad("Nivel Primario", VARONES))
#print("Mujeres primaria:", cantidad("Nivel Primario", MUJERES))

#print("Varones secundaria:", cantidad("Nivel Secundario", VARONES))
#print("Mujeres secundaria:", cantidad("Nivel Secundario", MUJERES))

#print("Varones inicial:", cantidad("Nivel Inicial", VARONES))
#print("Mujeres inicial:", cantidad("Nivel Inicial", MUJERES))



