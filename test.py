from proyecto import *

def estructura_datos()->dict:
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

def test_cantidad_valores():
    diccionario=estructura_datos()
    assert cantidad_valores(diccionario, "municipio_nombre") == 21
    assert cantidad_valores(diccionario, "modalidad") == 21
    assert cantidad_valores(diccionario, "nivel") == 21


def test_tipos_valores():
    diccionario=estructura_datos()
    diccionario1 = {"colores": ["rojo", "azul", "rojo", "verde", "azul"]}
    assert tipos_valores(diccionario1, "colores") == ["rojo", "azul", "verde"]
    assert tipos_valores(diccionario, "nivel") == ["Nivel Secundario", "Nivel Inicial", "Nivel Primario", "Formación Integral"]


def test_datos_tabla_escuela():
    diccionario1 = {
                    "establecimiento_id": ["100", "200", "300"],
                    "establecimiento_nombre": ["Escuela Belgrano", "Escuela San Martín", "Jardín Sol"],
                    "nivel": ["Nivel Primario", "Nivel Secundario", "Nivel Inicial"],
                    "modalidad": ["Común", "Técnica", "Común"],
                    "direccion": ["Calle A", "Calle B", "Calle C"],
                    "municipio_nombre": ["Rosario", "San Lorenzo", "Funes"],
                    "email": ["a@gmail.com", "b@gmail.com", "c@gmail.com"],
                    "telefono": ["1111", "2222", "3333"],
                    "sector": ["Estatal", "Privado", "Estatal"],
                    "latitud": ["-32.9", "-32.8", "-32.7"],
                    "longitud": ["-60.7", "-60.6", "-60.5"]}

    diccionario2 =  {"Nombre": "Escuela Belgrano",
                        "Nivel": "Nivel Primario",
                        "Modalidad": "Común",
                        "Dirección": "Calle A",
                        "Municipio": "Rosario",
                        "Correo": "a@gmail.com",
                        "Teléfono": "1111",
                        "Sector": "Estatal",
                        "Latitud": "-32.9",
                        "Longitud": "-60.7"}

    assert datos_tabla_escuela(diccionario1, "100") == diccionario2

def test_cantidad_escuelas_nivel():
    diccionario=estructura_datos()
    assert cantidad_escuelas_nivel(diccionario, "Nivel Secundario") == 7

def test_indices_tabla_establecimientos():
    diccionario=estructura_datos()
    assert indices_tabla_establecimientos(diccionario, "Merlo", "Nivel Primario") == [19]
    assert indices_tabla_establecimientos(diccionario, "Azul", "Nivel Secundario") == []
    assert indices_tabla_establecimientos(diccionario, "Berazategui", "Nivel Primario") == []


def test_datos_tabla_establecimientos():
    diccionario=estructura_datos()
    assert datos_tabla_establecimientos(diccionario, "Escobar", "Nivel Secundario") ==  {'Dirección': [], 'E-mail': [], 'Nombre del Establecimiento': []}
    assert datos_tabla_establecimientos(diccionario, "Merlo", "Nivel Primario") == {'Dirección': ["BACH E /FREIRE Y NERVO - S/N"], 'E-mail': ["primaria66merlo@abc.gob.ar"], 'Nombre del Establecimiento':['ESCUELA DE EDUCACIÓN PRIMARIA Nº66 "PABLO PIZZURNO"']}

def test_calculo_suma():
    diccionario=estructura_datos()
    assert calculo_suma([1.1, 5.2, 3.3]) == 9.6
    assert calculo_suma([0]) == 0.0


