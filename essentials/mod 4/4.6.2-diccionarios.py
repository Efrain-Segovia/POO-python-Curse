#diccionarios

mi_diccionario_3 = {
    "que paso": "baax uch", 
    "Axila": "Xic", 
    "Cabeza": "Pool", 
    "Garrapata": "Pech"
    }

# print(mi_diccionario)

#buscar por clave: key
# print(mi_diccionario_3["Cabeza"])
# print(mi_diccionario_3.get("Axila"))

# mi_diccionario = {
#     "nombre": "Juan",
#     "edad": 30,
#     "ciudad": "Madrid"
#     }
# #agregar o modificar elementos
# mi_diccionario["profesion"] = "Ingeniero"  # Agregar nueva clave-valor
# mi_diccionario["edad"] = 31  # Modificar valor existente
# print(mi_diccionario)

# #recorrido de diccionarios
dictionary = {"gato": "cat", "perro": "dog", "caballo": "horse"}

# #usando keys()
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

#usandodo items()
# for spanish, ingles in dictionary.items():
#     print(spanish, "->",ingles)

mi_diccionario_2 = {
    "nombre": "Lucio",
    "edad": 21,
    "ciudad": "Merida",
    "profesion": "Ingeniero"
}
print(mi_diccionario_2)

#modificar elementos
mi_diccionario_2["edad"] = 22  # Modificar valor existente
print(mi_diccionario_2)

#Agregando nuevas llaves
mi_diccionario_2["telefono"] = "999501123"
print(mi_diccionario_2)
#update
mi_diccionario_2.update({"email": "lucio@example.com", "edad": 23})
print(mi_diccionario_2)

# <---------->

#eliminar elementos
del mi_diccionario_2["ciudad"]  # Eliminar por clave
print(mi_diccionario_2)  

#eliminar el ultimo elemento insertado
mi_diccionario_2.popitem()
print(mi_diccionario_2) 

lst = [1,2,3,4]
