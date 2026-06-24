from proyecto import (estructura_datos,cantidad_valores,tipos_valores,niveles_modalidad,agregar_datos)

#Cargar los datos una sola vez
diccionario = estructura_datos()


def test_cantidad_valores():
    assert cantidad_valores(diccionario, "nivel") == 12000


def test_tipos_y_niveles():
    # Debe existir la modalidad "Educación Común"
    assert "Educación Común" in tipos_valores(diccionario, "modalidad")

    # Debe haber escuelas de Nivel Primario en Educación Común
    assert len(niveles_modalidad(diccionario,"Nivel Primario","Educación Común")) > 0


def test_agregar_datos():
    niveles = ["Nivel Secundario\nEducación Común", "Nivel Inicial\nEducación Común"]
    sexo = {"Varones": [], "Mujeres": []}

    agregar_datos(diccionario, "Nivel Primario", "Educación Común", niveles, sexo)

    assert len(niveles) == 3
    assert niveles[2] == "Nivel Primario\nEducación Común"
    assert sexo["Varones"][0] > 0
    assert sexo["Mujeres"][0] > 0