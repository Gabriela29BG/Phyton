nombre = "lucas"
nombre = "dalto"
print(nombre)

#asi se concatena strings
bienvenida = "HOLA" + nombre + "COMO ESTAS?"
print(bienvenida)

#asi se concatena con otros tipos de variables
numero = 3
bienvenida = f"hola {numero} como estas? "
print(bienvenida)

#snake-case
nombre_completo_master = "lol"

nombre = True
#asi se concatenan variables que no son strings
bienvenida = f"hola {nombre} como estas"
#borra lasvrables
del bienvenida
print(bienvenida)

#operadores deperenencia (in// not in)
print("lucas" in bienvenida)#true
print("lucas" in bienvenida)#flse

