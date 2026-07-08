import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl

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

def ingreso_establecimiento_id(diccionario:dict)-> str:
    #Toma un diccionario y le pide al usuario que ingrese el id del establecimiento del cual desea obtener más 
    #información. Devuelve un str numérico que corresponde al id si el id ingresado existe, sino devuelve "".
    id=st.text_input("Por favor, ingrese el id del establecimiento: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
                    on_change=None, args=None, kwargs=None, placeholder="Ingrese el id del establecimiento.", disabled=False, 
                    label_visibility="visible", icon=None, width="stretch", bind=None)
    if id in diccionario["establecimiento_id"]:
        return id
    else:
        return ""
            
def x_escuela(diccionario: dict, credencial="" ) -> dict:
    #Toma un diccionario y el id del establecimiento eductivo (str) y devuelve un diccionario con los datos
    #mas relevantes del establecimiento.
    if credencial != "":
        for i in range(cantidad_valores(diccionario, "establecimiento_id")):
            if diccionario["establecimiento_id"][i] == credencial:
                diccionario_tabla= {
                "establecimiento_nombre": diccionario["establecimiento_nombre"][i],
                "nivel": diccionario["nivel"][i],
                "modalidad": diccionario["modalidad"][i],
                "direccion": diccionario["direccion"][i],
                "municipio": diccionario["municipio_nombre"][i],
                "correo": diccionario["email"][i],
                "telefono": diccionario["telefono"][i],
                "sector": diccionario["sector"][i],
                "latitud": diccionario["latitud"][i],
               "longitud": diccionario["longitud"][i]}
                return diccionario_tabla
        return {}
    return None


def tabla(diccionario_tabla: dict, credencial=""):
    #Toma un diccionario y el id del establecimiento educativo (str) y si es distinto de "", muestra una tabla
    #con los datos más relevantes del establecimiento.
    if credencial != "":
        return st.table(data=diccionario_tabla, border=True, width="stretch", height="content", 
                        hide_index=None, hide_header=None)
    return None

def mapa(diccionario_tabla:dict,credencial=""):
    #Toma un diccionario y el id del establecimiento eductivo (str) e imprime un mapa con un punto en la 
    #coordenada donde se halla el establcimiento.
    if credencial != "":
        lat=diccionario_tabla["latitud"]
        long=diccionario_tabla["longitud"]
        st.map(data={"lat": [float(lat)], "lon": [float(long)]}, latitude=None, longitude=None, 
           color=None, size=None, zoom=None, width="stretch", height=500, use_container_width=None)
    return None

def ingreso_municipio_nombre(diccionario:dict)-> str:
    #Toma un diccionario y le pide al usuario que ingrese el nombre del municipio del cual desea obtener más 
    #información. Devuelve un str que corresponde al municipio, si el municipio no existe, sino devuelve "".
    introduccion="Establecimientos por localidad y nivel educativo: "
    st.header(introduccion, anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    municipio=st.text_input("Por favor, ingrese el nombre del municipio: ", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, 
                    on_change=None, args=None, kwargs=None, placeholder="Ingrese el nombre del municipio", disabled=False, 
                    label_visibility="visible", icon=None, width="stretch", bind=None)
    i = 0
    while i < cantidad_valores(diccionario, "municipio_nombre"):
        if municipio.lower() == diccionario["municipio_nombre"][i].lower():
            return municipio
        i += 1

    return ""

def ingreso_nivel(diccionario:dict)->str:
    #Toma un diccionario y le pide al usuario que seleccione el nivel del establecimiento del cual desea obtener más 
    #información. Devuelve un str que corresponde al nivel.
    nivel=st.radio("Seleccione un nivel educativo: ", tipos_valores(diccionario, "nivel"), index=None, key=None, help=None, on_change=None,
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


#¿Cuántas escuelas hay en la provincia de Buenos Aires dependiendo su nivel?

def cantidad_escuelas_nivel(diccionario:dict, nivel:str)-> int:
    '''esta funcion toma un diccionario y devuelve la cantidad de escuelas que hay 
    dependiendo el nivel
    cantidad_escuelas_nivel(diccionario, "Nivel Secundario") == 7
    cantidad_escuelas_nivel([], "Nivel Secundario") == 0
    cantidad_escuelas_nivel(diccionario, "Formacion Intregal") == 1'''
    cantidad = 0
    for niv in diccionario["nivel"]:
        if niv == nivel:
            cantidad +=1
        
    return cantidad

def selector_niveles(diccionario:dict):
    #crea un selector de cajas con los niveles posibles y devuelve la cantidad de escuelas de ese nivel
    nivel = st.selectbox("Por favor, seleccione un nivel educativo:",
                          tipos_valores(diccionario, "nivel"),
                          index = None,
                          placeholder="Seleccione un nivel educativo.")
    if nivel is not None:
        cant = cantidad_escuelas_nivel(diccionario, nivel)
        st.write("Hay " + str(cant) + " escuelas de " + nivel + " en la Provincia de Buenos Aires.")


#¿En el municipio Y, como están distribuidas porcentualmente los distintos niveles de escuelas?

def ingreso_municipio_selector(diccionario:dict):
    municipio=st.selectbox("Por favor, seleccione el municipio:", tipos_valores(diccionario, "municipio_nombre"), 
                           index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None,
                           disabled=False, label_visibility="visible", accept_new_options=False, filter_mode="fuzzy", 
                           width="stretch", bind=None)
    return municipio


def grafico_torta_municipio(diccionario: dict):
    municipio=ingreso_municipio_selector(diccionario)
    if municipio == "":
        return
    sizes=[]
    labels=[]
    for nivel in tipos_valores(diccionario, "nivel"):
        indices = indices_tabla_establecimientos(diccionario, municipio, nivel)
        if indices!=[]:
            sizes.append(len(indices))
            labels.append(nivel)

    colores=["#7b1fa2", "#5c6bc0", "#26c6da", "#9ccc65", "#ef5350", "#ff7043", "#ffca28"]
    propiedades_porciones = {'linewidth': 2, 'edgecolor': 'white'}
    propiedades_texto = {'fontsize': 10}

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=None, labels=labels, colors=colores, autopct='%1.1f%%', pctdistance=0.6, shadow=False, 
             labeldistance=1.1, startangle=90, radius=1, counterclock=True, wedgeprops=propiedades_porciones, textprops=propiedades_texto, 
             center=(0, 0), frame=False, rotatelabels=False, normalize=True, hatch=None, data=None)
    ax.set_title(f"Distribución de establecimientos por nivel en {municipio}:")
    st.pyplot(fig)

#Mostrar la información resumida de escuelas rurales, detallando por cada municipio la siguiente información:
#¿Cuantas hay ?
#¿Cuantas son publicas? y Cuántas son privadas?
#¿Cuantos estudiantes asisten a estas escuelas?

def escuelas_rurales_lista(diccionario:dict, municipio:str)-> dict:
    #Toma un diccionario y devuelve un diccionario que especifica la cantidad de escuelas rurales por municipio, cuántas
    #son públicas, cuántas son privadas y la cantidad de alumno que tienen.
    cantidad_escuelas_rurales=0
    cantidad_alumnos=0
    cantidad_publicas=0
    cantidad_privadas=0
    lista_escuelas_rurales= [municipio, cantidad_escuelas_rurales, cantidad_alumnos, cantidad_publicas, cantidad_privadas]
    for indice in range(cantidad_valores(diccionario, "municipio_nombre")):
        if diccionario["municipio_nombre"][indice] == municipio and (diccionario["ambito"][indice] == "Rural Agrupado" or diccionario["ambito"][indice] == "Rural Disperso"):
            cantidad_escuelas_rurales+=1
            cantidad_alumnos+=int(diccionario["matricula"][indice])
            if diccionario["sector"][indice]=="Estatal":
                cantidad_publicas+=1
            else: 
                cantidad_privadas+=1

            lista_escuelas_rurales= [municipio, cantidad_escuelas_rurales, cantidad_alumnos, cantidad_publicas, cantidad_privadas]
    return lista_escuelas_rurales

def escuelas_rurales_diccionario(diccionario:dict)->dict:
    diccionario_escuelas_rurales={
        "Municipio":[],
        "Cantidad de Escuelas Rurales":[],
        "Cantidad de Alumnos":[],
        "N° de Escuelas Rurales Estatales":[],
        "N° de Escuelas Rurales Privadas":[]
    }
    for municipio in tipos_valores(diccionario,"municipio_nombre"):
        lista_datos=escuelas_rurales_lista(diccionario,municipio)
        diccionario_escuelas_rurales["Municipio"].append(lista_datos[0])
        diccionario_escuelas_rurales["Cantidad de Escuelas Rurales"].append(lista_datos[1])
        diccionario_escuelas_rurales["Cantidad de Alumnos"].append(lista_datos[2])
        diccionario_escuelas_rurales["N° de Escuelas Rurales Estatales"].append(lista_datos[3])
        diccionario_escuelas_rurales["N° de Escuelas Rurales Privadas"].append(lista_datos[4])

    return diccionario_escuelas_rurales

def tabla_escuelas_rurales(diccionario_escuelas_rurales: dict):
    #Toma un diccionario y el id del establecimiento educativo (str) y si es distinto de "", muestra una tabla
    #con los datos más relevantes del establecimiento.
    tabla_escuelas_rurales= st.table(data=diccionario_escuelas_rurales, border=True, width="stretch", height="content", 
                        hide_index=None, hide_header=None)
    return tabla_escuelas_rurales


def main():
    #Entrada y salida de datos.
    diccionario = estructura_datos()
    st.set_page_config(layout="wide")
    st.title("Escuelas de la Provincia de Buenos Aires", anchor=None, help=None, width="stretch", text_alignment="center")

    st.header("Información y ubicación del establecimiento en base a su id.", anchor=None, help=None, divider=False, 
                  width="stretch", text_alignment="center")
    credencial=ingreso_establecimiento_id(diccionario)
    pregunta1=st.expander("Seleccione para ver más.",
                          expanded=True, key=None, icon=None, type="default", width="stretch", on_change="ignore", 
                        args=None, kwargs=None)     
    with pregunta1:
        diccionario_tabla=x_escuela(diccionario, credencial)
        tabla(diccionario_tabla, credencial)
        mapa(diccionario_tabla,credencial)

    st.header("Cantidad de escuelas por Nivel Educativo.", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    selector_niveles(diccionario)

    municipio=ingreso_municipio_nombre(diccionario)
    nivel=ingreso_nivel(diccionario)
    pregunta2=st.expander("Seleccione para ver más.",
                expanded=False, key=None, icon=None, type="default", width="stretch", on_change="ignore", 
                args=None, kwargs=None)     
    with pregunta2:
        if municipio!="" and nivel!="":
            tabla_establecimientos(diccionario,municipio,nivel)  
    
    
        
    col1, col2 = st.columns(2,gap="medium", vertical_alignment="top", border=False, width="stretch")
    with col1:
        st.header("¿En el municipio seleccionado, como están distribuidas porcentualmente los distintos niveles de escuelas?", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        grafico_torta_municipio(diccionario)
    with col2:
        st.header("¿Cuántos varones y mujeres hay en las escuelas de nivel inicial, secundario y primario, de la provincia de Buenos Aires, separadas por modalidad de la escuela?", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        grafico(diccionario)
        
        
    st.header("Información sobre Escuelas Rurales.", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    pregunta3=st.expander("Seleccione para ver más.",
                          expanded=False, key=None, icon=None, type="default", width="stretch", on_change="ignore", 
                        args=None, kwargs=None)     
    with pregunta3:
        diccionario_escuelas_rurales=escuelas_rurales_diccionario(diccionario)
        tabla_escuelas_rurales(diccionario_escuelas_rurales)
   

    




        


main() 