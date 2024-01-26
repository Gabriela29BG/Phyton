cadena1 = "hola soy gaby"
cadena2 ="Bienvenido lol"

print(dir(4)) #con esta funcion se puede ver los metodos que se pueden aplicr

#estructura de como aplicar los meodos
#resultado = DATO. METODO (PARAMETRO)

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayusculas
primer_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("D")

#buscado una cadena en otra cadena, si no hay coincidencias laza una excepcion
busqueda_index = cadena1.index("D")

#si es numerico devolvemos true, sino devolvemos falso
es_numerico = cadena1.isnumeric()

#si es alfanmerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

 #contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
 contar_coincidencias = cadena1.count("la ma")

#contamos cuenos caracteres tiene uns cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
eempieza-con = cadena1.startswith("H")

#si el valor 1, se encuentra en la cadena originall, remplaza el valor 1 de lamisma, ppor el valor 2
termina_con =cadena1.endswith("H")

#si el valor 1, se
