import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt


'''st.title("Proyecto Grupal de programacion")
st.write("Empecemos a trabajar equipo!")'''


#lectura del dataset
escuelas = []
with open("establecimientos-educativos-12K.csv", newline='') as escuelas_ba:
    lector = csv.reader(escuelas_ba)

    for escuela in lector:
        escuelas.append(escuela)
 

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

print("Varones primaria:", cantidad("Nivel Primario", VARONES))
print("Mujeres primaria:", cantidad("Nivel Primario", MUJERES))

print("Varones secundaria:", cantidad("Nivel Secundario", VARONES))
print("Mujeres secundaria:", cantidad("Nivel Secundario", MUJERES))

print("Varones inicial:", cantidad("Nivel Inicial", VARONES))
print("Mujeres inicial:", cantidad("Nivel Inicial", MUJERES))



