import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt

#Para ejecutar el programa: 
#pip install streamlit
#python -m streamlit run proyecto.py


def estructura_datos()->dict:
  #  "Toma el archivo .csv, lee las filas, arma listas en base a las columnas y devuelve un diccionario donde"
  #  "la clave son str de los titulos provistos en la fila 0 del archivo.csv y el valor es una lista con los demás"
  #  "valores de la columna."
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
        varones=[]
        mujeres=[]
        turnos=[]
        latitud=[]
        longitud=[]

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
            latitud.append(escuela[33])
            longitud.append(escuela[34])
        
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
                        turnos[0]:turnos[1:],
                        latitud[0]:latitud[1:],
                        longitud[0]:longitud[1:]}
    
    return diccionario

#print(estructura_datos())
    
def cantidad_valores(diccionario:dict, clave:str)->int:
    '''Toma una clave del diccionario y evalua cuántos elementos posee la lista que 
    representa su valor.'''

    return len(diccionario[clave])


def tipos_valores(diccionario:dict, clave:str) -> list:
#Toma una clave del diccionario y genera una lista con los diferentes tipos de elementos posee la lista que 
#representa su valor.
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



def agregar_datos(diccionario: dict, nivel: str, modalidad: str,niveles: list, sexo: dict):
    '''esta funcion agrega los niveles donde los chicos (varones y nenas) son distinto de 0, a la lista niveles
    donde se guardan los nombres que aparecen en el eje x...por otra parte calcula los chicos y chicas por nivel y modalidad
     para guardar en el diccionario sexo que despues se usa en el grafico '''

    indices = niveles_modalidad(diccionario, nivel, modalidad)

    cantidad_varones = suma_matricula_sexo(diccionario, indices, "varones")
    cantidad_mujeres = suma_matricula_sexo(diccionario, indices, "mujeres")

    if cantidad_varones != 0 or cantidad_mujeres != 0:
        niveles.append(f"{nivel}\n{modalidad}")
        sexo["Varones"].append(cantidad_varones)
        sexo["Mujeres"].append(cantidad_mujeres)

def grafico(diccionario: dict):
    '''esta funcion toma el diccionario general y utilizando la funcion anterior, toma valores
    necesarios para hacer el grafico'''
    niveles = []
    sexo = {"Varones": [], "Mujeres": []}

    for nivel in ["Nivel Secundario", "Nivel Primario", "Nivel Inicial"]:
        for modalidad in tipos_valores(diccionario, "modalidad"):
            agregar_datos(diccionario, nivel, modalidad, niveles, sexo)


#PARTE DEL MATPLOT
    fig, ax = plt.subplots(figsize=(18, 10), layout="constrained")
    ax.set_xticklabels(niveles, rotation=90,fontsize=15)
    res = ax.grouped_bar(sexo, tick_labels=niveles, group_spacing=1,colors=["navy","skyblue"])
    for container in res.bar_containers:
        ax.bar_label(container, padding=3,fontsize=15)

    ax.set_ylabel('Cantidad de Estudiantes',fontsize=20)
    ax.legend(loc='upper left', ncols=2,fontsize=20)
    ax.set_ylim(0, 500000)

    st.pyplot(fig)

#NO UTILIZADAs
#def conversion_str_float(clave:str,diccionario:dict)->list:
#   Toma una lista de str y la convierte a una lista de float.
#    list_float=[]
#    for x in diccionario[clave]:
#        list_float.append(float(x))
#    return list_float

#def buscador_indices(diccionario:dict,clave:str,dato:Any)->int:
#   Toma un diccionario cuyos valores sean listas, una clave de ese diccionario y un dato que 
#   pertenece a los valores de esa clave y devuelve el indice del lugar que ocupa en la lista.
#    for i in range (0,cantidad_valores(diccionario,clave)):
#        if dato == diccionario[clave][i]:
#            return i

def mapa(diccionario:dict,credencial=""):
    #Toma un diccionario y el id del establecimiento eductivo (str) e imprime un mapa con un punto en la 
    #coordenada donde se halla el establcimiento.
    if credencial != "":
        i=x_escuela(diccionario, credencial)["latitud"]
        j=x_escuela(diccionario, credencial)["longitud"]
        st.map(data={"lat": [float(i)], "lon": [float(j)]}, latitude=None, longitude=None, 
           color=None, size=None, zoom=None, width="stretch", height=500, use_container_width=None)
    return None
            
def x_escuela(diccionario: dict, credencial="" ) -> dict:
    #Toma un diccionario y el id del establecimiento eductivo (str) y devuelve un diccionario con los datos
    #mas relevantes del establecimiento.
    if credencial != "":
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
                "sector": diccionario["sector"][i],
                "latitud": diccionario["latitud"][i],
               "longitud": diccionario["longitud"][i]
            }
        return {}
    return None


def tabla(diccionario: dict, credencial=""):
    #Toma un diccionario y el id del establecimiento educativo (str) y si es distinto de "", muestra una tabla
    #con los datos más relevantes del establecimiento.
    if credencial != "":
        return st.table(data=x_escuela(diccionario,credencial), border=True, width="stretch", height="content", 
                        hide_index=None, hide_header=None)
    return None



def ingreso_establecimiento_id(diccionario:dict)-> str:
    #Toma un diccionario y le pide al usuario que ingrese el id del establecimiento del cual desea obtener más 
    #información. Devuelve un str numérico que corresponde al id si el id ingresado existe, sino devuelve "".
    id=st.text_input("Por favor, ingrese el id del establecimiento: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
                    on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, 
                    label_visibility="visible", icon=None, width="stretch", bind=None)
    if id in diccionario["establecimiento_id"]:
        return id
    else:
        return ""

def ingreso_municipio_nombre(diccionario:dict)-> str:
    #Toma un diccionario y le pide al usuario que ingrese el nombre del municipio del cual desea obtener más 
    #información. Devuelve un str que corresponde al municipio, si el municipio no existe, sino devuelve "".
    introduccion="Establecimientos por localidad y nivel educativo: "
    st.header(introduccion, anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    municipio=st.text_input("Por favor, ingrese el nombre del municipio: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
                    on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, 
                    label_visibility="visible", icon=None, width="stretch", bind=None)
    for i in range (0,cantidad_valores(diccionario,"municipio_nombre")):
        if municipio.lower() == diccionario["municipio_nombre"][i].lower():
            return municipio
    else:
        return ""

def ingreso_nivel(diccionario:dict)->str:
    #Toma un diccionario y le pide al usuario que seleccione el nivel del establecimiento del cual desea obtener más 
    #información. Devuelve un str que corresponde al nivel.
    nivel=st.radio("Seleccione un nivel educativo: ", tipos_valores(diccionario, "nivel"), index=0, key=None, help=None, on_change=None,
     args=None, kwargs=None, disabled=False, horizontal=False, captions=None, label_visibility="visible", 
     width="content", bind=None)
    return nivel
    
def indices_tabla_establecimientos(diccionario:dict,municipio:str,nivel:str)->list:
    #Toma un diccionario, el str del municipio y el str del nivel y devuelve la posicion de las listas de los 
    #establecimientos que cumplen ambas condiciones (municipio y nivel).
    indices=[]
    for j in range (0,cantidad_valores(diccionario, "municipio_nombre")):
        if municipio.lower() == diccionario["municipio_nombre"][j].lower() and nivel == diccionario["nivel"][j]:
            indices.append(j)
    return indices
   
def datos_tabla_establecimientos(diccionario:dict,municipio:str,nivel:str)->dict:
    #Toma un diccionario, el municipio (str) y el nivel (str) y devuelve un diccionario con los datos del nombre
    #del establecimiento, dirección y el email de los establecimientos que son del municipio ingresado y del nivel
    #seleccionado.
    indices=indices_tabla_establecimientos(diccionario,municipio,nivel)
    establecimiento_nombre=[]
    direccion=[]
    email=[]
    for j in indices:
        establecimiento_nombre.append(diccionario["establecimiento_nombre"][j])
        direccion.append(diccionario["direccion"][j])
        email.append(diccionario["email"][j])
    datos_tabla={"Nombre del Establecimiento":establecimiento_nombre,"Dirección":direccion,"E-mail":email}
    return datos_tabla

def tabla_establecimientos(diccionario:dict,municipio:str,nivel:str):
    #Toma un diccionario, el municipio y el nivel y muestra una tabla con los datos del nombre del establecimiento, 
    #dirección y el email de los establecimientos que son del municipio ingresado y del nivel seleccionado.
    datos_tabla=datos_tabla_establecimientos(diccionario, municipio, nivel)
    if len(datos_tabla["Nombre del Establecimiento"]) > 0:
        tabla=st.table(data=datos_tabla, border=True, width="stretch", height="content",
         hide_index=None, hide_header=None)
        return tabla
    else: 
        texto="No existen establecimientos de tal nivel en la localidad ingresada."
        st.markdown(texto, unsafe_allow_html=False, help=None, width="auto", text_alignment="left")


def main():
    diccionario = estructura_datos()
    st.set_page_config(layout="wide")
    st.title("Escuelas de la Provincia de Buenos Aires", anchor=None, help=None, width="stretch", text_alignment="center")
    col1, col2 = st.columns(2,gap="medium", vertical_alignment="top", border=False, width="stretch")
    with col1:
        st.header("Información y ubicación del establecimiento en base a su id.", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        credencial=ingreso_establecimiento_id(diccionario)
        tabla(diccionario, credencial)
        mapa(diccionario,credencial)
        municipio=ingreso_municipio_nombre(diccionario)
        nivel=ingreso_nivel(diccionario)
        if municipio!="" and nivel!="":
            tabla_establecimientos(diccionario,municipio,nivel)  
    with col2:
        st.header("¿Cuántos varones y mujeres hay en las escuelas de nivel inicial, secundario y primario, de la provincia de Buenos Aires, separadas por modalidad de la escuela?", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        grafico(diccionario)
        


main() 