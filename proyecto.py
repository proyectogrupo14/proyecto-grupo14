import csv
import codecs
import streamlit as st
st.title("Proyecto Grupal de programacion")
st.write("Empecemos a trabajar equipo!")


#lectura del dataset
escuelas = []
with open("establecimientos-educativos-12K.csv", newline='') as escuelas_ba:
    lector = csv.reader(escuelas_ba)

    for escuela in lector:
        escuelas.append(escuela)


#nenes en total
def hombres_escuela():
    nenes = 0
    for escuela in escuelas[1:]:
        nenes = nenes + int(escuela[26])
    return nenes
print("los varones son:", hombres_escuela())

#nenas en total
def mujeres_escuela():
    nenas = 0
    for escuela in escuelas[1:]:
        nenas = nenas + int(escuela[27])
    return nenas
print("los mujeres son:", mujeres_escuela())




