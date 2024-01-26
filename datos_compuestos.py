#creando una lista (se pueden modificar)
lista = ["uno, dos, tres, true, 1.8"]

#creando una tupla no se puede modificar)
tupla = ("uno, dos, tres, tre, 1.8")

#esto es valido con las listas pero con las tuplas
lista[3] = "maquinola"

print(lista[3])

#creando un conjunto (set), (no se accede a elemeno por indice,
# no almacena datos duplicados)
conjunto = {"uno, dos, tres"}

#print(conjunto[3]) = no se puede acceder al elemento

#creando un diccionario (dict)
diccionario = {
    'nombre' : "gaby",
    'canal' : "soy gaby",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "soy dalto"
}

print(diccionario['altura'])
