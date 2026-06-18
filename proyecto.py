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

def estructura_datos():
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
        varones=[]
        mujeres=[]
        turnos=[]

        for escuela in escuelas_ba:
            municipio_id.append(escuela[0])	
            municipio_nombre.append(escuela[1])
            establecimiento_id.append(escuela[2])
            establecimiento_nombre.append(escuela[3])
            modalidad.append(escuela[7])
            nivel.append(escuela[8])
            direccion.append(escuela[9])
            telefono.append(escuela[10])
            email.append(escuela[12])
            sector.append(escuela[13])
            tipo_organizacion.append(escuela[15])
            ambito.append(escuela[17])
            matricula.append(escuela[25])
            varones.append(escuela[26])
            mujeres.append(escuela[27])
            turnos.append(escuela[29])
        
        diccionario ={municipio_id[0]:municipio_id[1:],
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
                        varones[0]:varones[1:],
                        mujeres[0]:mujeres[1:],
                        turnos[0]:turnos[1:]}
    
    return diccionario

#print(estructura_datos().keys())
    
def cantidad_valores(diccionario:dict, clave:str)->int:
    '''Toma una clave del diccionario y evalua cuántos elementos posee la lista que 
    representa su valor.'''

    return len(diccionario[clave])


def tipos_valores(diccionario:dict, clave:str) -> list:

    tipos_valores=[]

    for i in diccionario[clave]:
        if i not in tipos_valores:
            tipos_valores.append(i)
    return tipos_valores



def niveles_modalidad(diccionario:dict, nivel: str, modalidad:str) -> list:
    """  Filtra y devuelve una lista con el nombre de los establecimientos que pertencen al nivel y modalidad introducidos.

    niveles("Primario") = 
    niveles("Secundario") = 
    niveles("Inicial") = Hoja de cálculo sin título - 
    """
    list_nivel = []

    for i in range (0,cantidad_valores(diccionario, "nivel")):
        if diccionario["nivel"][i] == nivel and diccionario["modalidad"][i] == modalidad:
            list_nivel.append(i)
    return list_nivel


def suma_matricula_sexo(diccionario:dict, ind_establecimiento: list, sexo: str) -> int:
   """ Calcula el total de alumnos de un sexo específico de una lista de establecimientos".

    suma([['Escuela     ]], ) = 10
    suma([['Escuela' ], ['Escuela' ,  ]],  ) = 
    suma([], ) = 0
   """
   
   suma=0
   for i in ind_establecimiento:
        if diccionario[sexo][i] != "":
            suma=suma+int(diccionario[sexo][i])
   return suma

#print(suma_matricula_sexo(niveles_modalidad('Nivel Secundario',"Educación Común"),"varones"))


#¿Cuántos varones y mujeres hay en las escuelas de nivel inicial, secundario y primario de la provincia de Buenos Aires,
#separadas por modalidad de la escuela?

def grafico(diccionario):
    niveles = []
    sexo = {
        "Varones":[],
        "Mujeres":[]
    }

    for nivel in ["Nivel Secundario", "Nivel Primario", "Nivel Inicial"]:
        
        for modalidad in tipos_valores(diccionario, "modalidad"):
            niveles.append(f"{nivel}\n{modalidad}")

            indices = niveles_modalidad(diccionario, nivel, modalidad)

            cantidad_varones = suma_matricula_sexo(diccionario, indices, "varones")
            cantidad_mujeres = suma_matricula_sexo(diccionario, indices, "mujeres")

            sexo["Mujeres"].append(cantidad_mujeres)
            sexo["Varones"].append(cantidad_varones)
#PARTE DEL MATPLOT
    fig, ax = plt.subplots(figsize=(18, 10), layout="constrained")
    ax.set_xticklabels(niveles, rotation=45)
    res = ax.grouped_bar(sexo, tick_labels=niveles, group_spacing=1)
    for container in res.bar_containers:
        ax.bar_label(container, padding=3)

    #ax.set_ylabel('Cantidad de Estudiantes')
    #ax.set_title("¿Cuántos varones y mujeres hay en las escuelas de nivel inicial, secundario y primario,de la provincia de Buenos Aires, separadas por modalidad de la escuela?")
    #ax.legend(loc='upper left', ncols=2)
    #ax.set_ylim(0, 250)

    st.pyplot(fig)
            
def x_escuela(diccionario: dict, credencial: str) -> dict:

    
    for i in range(cantidad_valores(diccionario, "establecimiento_id")):
        if diccionario["establecimiento_id"][i] == credencial:
            return {
                "establecimiento_nombre": diccionario["establecimiento_nombre"][i],
                "nivel": diccionario["nivel"][i],
                "modalidad": diccionario["modalidad"][i],
                "direccion": diccionario["direccion"][i],
                "municipio": diccionario["municipio_nombre"][i],
                "correo": diccionario["email"][i],
                "telefono": diccionario["telefono"][i],
                "sector": diccionario["sector"][i]
            }

    return {}


def main():
    diccionario = estructura_datos()
    grafico(diccionario)
    credencial = input("ingrese credencial:" )
    escuela = x_escuela(diccionario, credencial)
    print(escuela)

main() 