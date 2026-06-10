import codecs
import streamlit as st
st.title("Proyecto Grupal de programacion")
st.write("Empecemos a trabajar equipo!")


#lectura del dataset
escuelas = []
escuelas_BA = open("establecimientos-educativos-12K.csv")
for linea in escuelas_BA:
    escuela = linea.strip().split(',')
    escuelas.append(escuela)

def hombres_escuela():
    nenes = 0
    for escuela in escuelas[1:]:
        nenes += int(escuela[26])
    return nenes
print(hombres_escuela())