import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt


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

    
def cantidad_valores(diccionario:dict, clave:str)->int:
    #Toma una clave del diccionario y evalua cuántos elementos posee la lista que 
    #representa su valor.
    #EJ con archivo prueba: cantidad_valores(diccionario, "municipio_nombre") == 22
    #                       cantidad_valores(diccionario, "modalidad") == 22
    #                       cantidad_valores(diccionario, "nivel") == 22

    return len(diccionario[clave])


def tipos_valores(diccionario:dict, clave:str) -> list:
    #Toma una clave del diccionario y genera una lista con los diferentes tipos de elementos posee la lista que 
    #representa su valor.
    #EJ: diccionario1 = {"colores": ["rojo", "azul", "rojo", "verde", "azul"]}
    #    tipos_valores(diccionario, "colores") == ["rojo", "azul", "verde"]
    tipos_valores=[]
    for i in diccionario[clave]:
        if i not in tipos_valores:
            tipos_valores.append(i)
    return tipos_valores

#--------------------------------------------------------
#Información y ubicación de la escuela número X.
#--------------------------------------------------------

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
            
def datos_tabla_escuela(diccionario: dict, credencial="" ) -> dict:
    #Toma un diccionario y el id del establecimiento eductivo (str) y devuelve un diccionario con los datos
    #mas relevantes del establecimiento.
    #EJ:diccionario1 = {
    #                "establecimiento_id": ["100", "200", "300"],
    #                "establecimiento_nombre": ["Escuela Belgrano", "Escuela San Martín", "Jardín Sol"],
    #                "nivel": ["Nivel Primario", "Nivel Secundario", "Nivel Inicial"],
    #                "modalidad": ["Común", "Técnica", "Común"],
    #                "direccion": ["Calle A", "Calle B", "Calle C"],
    #                "municipio_nombre": ["Rosario", "San Lorenzo", "Funes"],
    #                "email": ["a@gmail.com", "b@gmail.com", "c@gmail.com"],
    #                "telefono": ["1111", "2222", "3333"],
    #                "sector": ["Estatal", "Privado", "Estatal"],
    #                "latitud": ["-32.9", "-32.8", "-32.7"],
    #                "longitud": ["-60.7", "-60.6", "-60.5"]}

    #datos_tabla_escuela(diccionario1, "100") == {"establecimiento_nombre": "Escuela Belgrano",
    #                                               "nivel": "Nivel Primario",
    #                                               "modalidad": "Común",
    #                                               "direccion": "Calle A",
    #                                               "municipio": "Rosario",
    #                                               "correo": "a@gmail.com",
    #                                               "telefono": "1111",
    #                                               "sector": "Estatal",
    #                                               "latitud": "-32.9",
    #                                               "longitud": "-60.7"}
    i=0
    if credencial != "":
        while i < cantidad_valores(diccionario, "establecimiento_id") and str(diccionario["establecimiento_id"][i]) != credencial:
            i+=1

    if str(diccionario["establecimiento_id"][i]) == credencial:    
        diccionario_tabla= {
            "Nombre": diccionario["establecimiento_nombre"][i],
            "Nivel": diccionario["nivel"][i],
            "Modalidad": diccionario["modalidad"][i],
            "Dirección": diccionario["direccion"][i],
            "Municipio": diccionario["municipio_nombre"][i],
            "Correo": diccionario["email"][i],
            "Teléfono": diccionario["telefono"][i],
            "Sector": diccionario["sector"][i],
            "Latitud": diccionario["latitud"][i],
            "Longitud": diccionario["longitud"][i]}
        return diccionario_tabla         
    return {}
    

def tabla_escuela(diccionario_tabla: dict, credencial=""):
    #Toma un diccionario y el id del establecimiento educativo (str) y si es distinto de "", muestra una tabla
    #con los datos más relevantes del establecimiento.
    if credencial != "":
        return st.table(data=diccionario_tabla, border=True, width="stretch", height="content", 
                        hide_index=None, hide_header=None)
    return None

def mapa_escuela(diccionario_tabla:dict,credencial=""):
    #Toma un diccionario y el id del establecimiento eductivo (str) e imprime un mapa con un punto en la 
    #coordenada donde se halla el establcimiento.
    if credencial != "":
        lat=diccionario_tabla["Latitud"]
        long=diccionario_tabla["Longitud"]
        st.map(data={"lat": [float(lat)], "lon": [float(long)]}, latitude=None, longitude=None, 
           color=None, size=None, zoom=None, width="stretch", height=500, use_container_width=None)
    return None

#----------------------------------------------------------------------------------------------------
#¿Cuántas escuelas hay en la provincia de Buenos Aires dependiendo su nivel y cuál es su localización?
#----------------------------------------------------------------------------------------------------

def cantidad_escuelas_nivel(diccionario:dict, nivel:str)-> int:
    #Toma un diccionario y devuelve la cantidad de escuelas que hay dependiendo el nivel educativo.
    #EJ con archivo de prueba:
    #cantidad_escuelas_nivel(diccionario, "Nivel Secundario") == 7
    cantidad = 0
    for niv in diccionario["nivel"]:
        if niv == nivel:
            cantidad+=1
        
    return cantidad


def selector_niveles(diccionario:dict):
# Genera un selector de cajas con los niveles educativos posibles y devuelve la cantidad de escuelas de ese nivel,
# una vez seleccionado el nivel, imprime un texto donde se datalla la cantidad de escuelas que existen en la provincia
# de Buenos Aires con tal nivel.
    nivel = st.selectbox("Por favor, seleccione un nivel educativo:",
                          tipos_valores(diccionario, "nivel"),
                          index = None,
                          placeholder="Seleccione un nivel educativo.")
    if nivel is not None:
        cant = cantidad_escuelas_nivel(diccionario, nivel)
        st.write("Hay " + str(cant) + " escuelas de " + nivel + " en la Provincia de Buenos Aires.")

        mapa_nivel(diccionario, nivel)


def mapa_nivel(diccionario: dict, nivel: str):
# Muestra en un mapa todas las escuelas del nivel educativo introducido.

    latitudes = []
    longitudes = []

    for i in range(cantidad_valores(diccionario, "nivel")):
        if (diccionario["nivel"][i] == nivel and
            diccionario["latitud"][i] != "" and
            diccionario["longitud"][i] != ""):

            latitudes.append(float(diccionario["latitud"][i]))
            longitudes.append(float(diccionario["longitud"][i]))

    st.map(data={"lat": latitudes,"lon": longitudes}, height=500)


#--------------------------------------------------------------------------------------------------
#¿Cuál es el nombre, dirección e e-mail de las instituciones educativas que se encuentran en Y municipio de la
# provincia de Buenos Aires, de X nivel educativo?
#-----------------------------------------------------------------------------------------------------

def ingreso_municipio_nombre(diccionario:dict)-> str:
#Toma un diccionario y le pide al usuario que ingrese el nombre del municipio del cual desea obtener más 
#información. Devuelve un str que corresponde al municipio, si el municipio no existe, sino devuelve "".
    
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
# Toma un diccionario y le pide al usuario que seleccione el nivel del establecimiento del cual desea obtener más 
# información. Devuelve un str que corresponde al nivel.
    nivel=st.radio("Seleccione un nivel educativo: ", tipos_valores(diccionario, "nivel"), index=None, key=None, help=None, 
    on_change=None, args=None, kwargs=None, disabled=False, horizontal=False, captions=None, label_visibility="visible", 
    width="content", bind=None)
    return nivel
    
def indices_tabla_establecimientos(diccionario:dict,municipio:str,nivel:str)->list:
# Toma un diccionario, el str del municipio y el str del nivel y devuelve una lista de indices de los establecimientos 
# que cumplen ambas condiciones (municipio y nivel).'''
#EJ con archivo de prueba:
# indices_tabla_establecimientos(diccionario, "Merlo", "Nivel Primario") == [19]
# indices_tabla_establecimientos(diccionario, "Azul", "Nivel Secundario") == []
# indices_tabla_establecimientos(diccionario, "Berazategui", "Nivel Primario") == []

    indices=[]
    for j in range (0,cantidad_valores(diccionario, "municipio_nombre")):
        if municipio.lower() == diccionario["municipio_nombre"][j].lower() and nivel == diccionario["nivel"][j]:
            indices.append(j)
    return indices
   
def datos_tabla_establecimientos(diccionario:dict,municipio:str,nivel:str)->dict:
#Toma un diccionario, el municipio (str) y el nivel (str) y devuelve un diccionario con los datos del nombre
#del establecimiento, dirección y el email de los establecimientos que son del municipio ingresado y del nivel
#seleccionado.
#EJ con archivo de prueba:
#datos_tabla_establecimientos(diccionario, "Escobar", "Nivel Secundario") ==  {'Dirección': [], 'E-mail': [],
# 'Nombre del Establecimiento': []}
#datos_tabla_establecimientos(diccionario, "Merlo", "Nivel Primario") == {'Dirección': ["BACH E /FREIRE Y NERVO - S/N"], 
#'E-mail': ["primaria66merlo@abc.gob.ar"], 'Nombre del Establecimiento':['ESCUELA DE EDUCACIÓN PRIMARIA Nº66 "PABLO PIZZURNO"']}

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
# Toma un diccionario, el municipio y el nivel y muestra una tabla con los datos del nombre del establecimiento, 
# dirección y el email de los establecimientos que son del municipio ingresado y del nivel seleccionado.'''
    datos_tabla=datos_tabla_establecimientos(diccionario, municipio, nivel)
    if len(datos_tabla["Nombre del Establecimiento"]) > 0:
        tabla=st.table(data=datos_tabla, border=True, width="stretch", height="content",
         hide_index=None, hide_header=None)
        return tabla
    else: 
        texto="No existen establecimientos de tal nivel en la localidad ingresada."
        st.markdown(texto, unsafe_allow_html=False, help=None, width="auto", text_alignment="left")

#----------------------------------------------------------------------
#¿En el municipio Y, como están distribuidas porcentualmente los distintos niveles de escuelas?
#----------------------------------------------------------------------

def ingreso_municipio_selector(diccionario:dict):
    municipio=st.selectbox("Por favor, seleccione el municipio:", tipos_valores(diccionario, "municipio_nombre"), 
                           index=0, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None,
                           disabled=False, label_visibility="visible", accept_new_options=False, filter_mode="fuzzy", 
                           width="stretch", bind=None)
    return municipio

def calculo_suma(sizes:list)->float:
    #Recibe una lista de float y devuelve la suma de los valores.
    #EJ: [1.1, 5.2, 3.3] -> 9.6
    #    [0] -> 0
    #    [8, 6, 1.3] -> 15.3
    cantidad=0
    for valor in sizes:
        cantidad+=valor
    return cantidad

def calculo_porcentaje(sizes:list)->list:
    #Recibe una lista de float y devuelve una lista de float con los porcentajes de los valores iniciales, redondeados
    #a 1 decimal.
    #EJ: [1.1, 5.2, 3.3] -> [11.5, 54.2, 34.4]
    #    [0] -> "Error, no se puede dividir por 0"
    #    [8, 6, 1.3] -> [52.3, 39.2, 8,5]
    lista_porcentaje=[]
    total=calculo_suma(sizes)
    if total != 0:
        for valor in sizes:
            porcentaje_float=(valor/total)*100
            porcentaje=round(porcentaje_float,1)
            lista_porcentaje.append(porcentaje)
        return lista_porcentaje
    else: 
        print("Error, no se puede dividir por 0")

def union_listas(lista1:list, lista2:list)->list:
    #Recibe una lista1 de str y una lista2 de float con porcentajes y devuelve una lista de str donde se detalla
    #una leyenda/nivel con su porcentaje asociado
    # EJ: [harina, azucar, huevo], [38, 52, 10] -> [harina (38%), azucar (52%), huevo (10%)]
    #     [inicial, primario, secundario], [51, 25, 24] -> [inicial (51%), primario (25%), secundario (24%)]
    #     [], [] -> []
    lista_total=[]
    for indice in range (0, len(lista1)):
        lista_total.append(lista1[indice]+" ("+str(lista2[indice])+"%)")
    return lista_total

def grafico_torta_municipio(diccionario: dict):
    #Dibuja un gráfico de tortas de la proporción de los niveles educativos según el municipio seleccionado.

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

    colores=plt.color_sequences['Paired']
    propiedades_porciones = {'linewidth': 1, 'edgecolor': 'white'}
    propiedades_texto = {'fontsize': 10}

    fig, ax = plt.subplots()
    grafico_tortas = ax.pie(sizes, explode=None, labels=None, colors=colores, autopct=None, pctdistance=0.6, shadow=False, 
                    labeldistance=1.1, startangle=90, radius=1, counterclock=True, wedgeprops=propiedades_porciones, textprops=propiedades_texto, 
                    center=(0, 0), frame=False, rotatelabels=False, normalize=True, hatch=None, data=None)

    lista_porcentaje=calculo_porcentaje(sizes)
    leyenda=union_listas(labels, lista_porcentaje)

    ax.legend(grafico_tortas.wedges, leyenda,
          title="Niveles Educativos",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)

#-------------------------------------------------------------------------------
#¿Cuántos varones y mujeres hay en las escuelas de nivel inicial, secundario y primario de la provincia de
# Buenos Aires, separadas por modalidad de la escuela?
#------------------------------------------------------------------------------

def lista_indices_modalidad(diccionario:dict, nivel:str, modalidad:str) -> list:
    """  Filtra y devuelve una lista con el indice de los establecimientos que pertencen al nivel 
    y modalidad introducidos.
    ejemplos:
    niveles_modalidad(diccionario, "Nivel Primario", "Educacion Comun") == [4,9,16,18,19,20]
    niveles_modalidad(diccionario, "Nivel Secundario", "Educacion Comun") ==[1,6,7,13]
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


def datos_grafico_barras(diccionario: dict, nivel: str) -> tuple:
#    Prepara un diccionario con los datos estructurados para el gráfico.
#   Devuelve también la lista de modalidades para usar en el eje X.

    modalidades = tipos_valores(diccionario, "modalidad")
    
    lista_varones = []
    lista_mujeres = []
    modalidades_grafico = []
    
    for modalidad in modalidades:
        indices = lista_indices_modalidad(diccionario, nivel, modalidad)
        cantidad_varones = suma_matricula_sexo(diccionario, indices, "varones")
        cantidad_mujeres = suma_matricula_sexo(diccionario, indices, "mujeres")
        
        if cantidad_varones > 0 or cantidad_mujeres > 0:
            lista_varones.append(cantidad_varones)
            lista_mujeres.append(cantidad_mujeres)
            modalidades_grafico.append(modalidad)
            
    datos_grafico = {f"Varones - {nivel}": lista_varones,
                     f"Mujeres - {nivel}": lista_mujeres}
    
    return datos_grafico, modalidades_grafico


def grafico_barras(diccionario: dict, nivel: str, color:str):
 #   Toma el diccionario y el nivel educativo, y dibuja el gráfico de barras.

    datos_grafico, modalidades = datos_grafico_barras(diccionario, nivel)

    fig, ax = plt.subplots(figsize=(18, 10), layout="constrained")
    ax.set_xticklabels(modalidades, rotation=25,fontsize=20)
    res = ax.grouped_bar(datos_grafico, tick_labels=modalidades, group_spacing=1,colors=color)
    for container in res.bar_containers:
        ax.bar_label(container, padding=3,fontsize=20)

    ax.set_ylabel('Cantidad de Estudiantes',fontsize=25)
    ax.legend(loc='upper right', ncols=2,fontsize=25)
    ax.set_ylim(0, 500000)

    st.pyplot(fig)

#---------------------------------------------------------------------------
#Mostrar la información resumida de escuelas rurales, detallando por cada municipio la siguiente información:
#¿Cuantas hay ?
#¿Cuantas son publicas? y Cuántas son privadas?
#¿Cuantos estudiantes asisten a estas escuelas?
#----------------------------------------------------------------

def escuelas_rurales_lista(diccionario:dict, municipio:str)-> dict:
    '''Toma un diccionario y devuelve un diccionario que especifica la cantidad de escuelas rurales por municipio, cuántas
    son públicas, cuántas son privadas y la cantidad de alumno que tienen.'''
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
    '''esta funcion toma la lista de municipios. 
    Llama a escuelas_rurales_lista() para cada municipio.
    Reúne todos los resultados en un único diccionario'''
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
    '''Toma un diccionario y el id del establecimiento educativo (str) y si es distinto de "", muestra una tabla
    con los datos más relevantes del establecimiento.'''
    tabla_escuelas_rurales= st.table(data=diccionario_escuelas_rurales, border=True, width="stretch", height="content", 
                        hide_index=None, hide_header=None)
    return tabla_escuelas_rurales


#-------------MAIN-------------------
def main():
    #Entrada y salida de datos.
    diccionario = estructura_datos()
    st.set_page_config(layout="wide")
    st.title("Escuelas de la Provincia de Buenos Aires", anchor=None, help=None, width="stretch", text_alignment="center")

    st.header("Información y ubicación del establecimiento en base a su id.", anchor=None, help=None, divider=False, 
                  width="stretch", text_alignment="center")
    credencial=ingreso_establecimiento_id(diccionario)
    col1, col2 = st.columns(2,gap="medium", vertical_alignment="top", border=False, width="stretch")
    with col1:
        pregunta1=st.expander("Seleccione para ver más.",
                          expanded=True, key=None, icon=None, type="default", width="stretch", on_change="ignore", 
                        args=None, kwargs=None)     
        with pregunta1:
            diccionario_tabla=datos_tabla_escuela(diccionario, credencial)
            tabla_escuela(diccionario_tabla, credencial)
    with col2:
        mapa_escuela(diccionario_tabla,credencial)

    st.header("Cantidad de establecimientos por Nivel Educativo.", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    selector_niveles(diccionario)

    introduccion="Establecimientos por Localidad y Nivel Educativo: "
    st.header(introduccion, anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    municipio=ingreso_municipio_nombre(diccionario)
    nivel=ingreso_nivel(diccionario)
    pregunta2=st.expander("Seleccione para ver más.",
                expanded=False, key=None, icon=None, type="default", width="stretch", on_change="ignore", 
                args=None, kwargs=None)     
    with pregunta2:
        if municipio!="" and nivel!="":
            tabla_establecimientos(diccionario,municipio,nivel)  

    st.header("¿En el municipio seleccionado, como están distribuidas porcentualmente los distintos niveles educativos de las instituciones?", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    grafico_torta_municipio(diccionario)
     
    st.header("¿Cuántos varones y mujeres hay en las escuelas de nivel inicial, secundario y primario, de la provincia de Buenos Aires, separadas por modalidad de la escuela?", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    col3, col4 = st.columns(2,gap="medium", vertical_alignment="center", border=False, width="stretch")
    with col3:
        grafico_barras(diccionario, "Nivel Inicial",["orange","moccasin"])
        grafico_barras(diccionario, "Nivel Primario",["green","limegreen"])
    with col4:
        grafico_barras(diccionario, "Nivel Secundario",["purple","orchid"])


        
    st.header("Información sobre Escuelas Rurales.", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
    pregunta3=st.expander("Seleccione para ver más.",
                          expanded=False, key=None, icon=None, type="default", width="stretch", on_change="ignore", 
                        args=None, kwargs=None)     
    with pregunta3:
        diccionario_escuelas_rurales=escuelas_rurales_diccionario(diccionario)
        tabla_escuelas_rurales(diccionario_escuelas_rurales)
   

main() 