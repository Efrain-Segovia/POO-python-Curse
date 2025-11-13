# # # Syntax simple
# numbers = [10, 5, 7, 2, 1]
# print(numbers)

# names = ["nahomy", "habib", "jesus", "Lucio", "erik", "mafer"]
# print(names)
# #funciones de listas
# print(len(names)) # longitud de la lista
# print(names[0]) # acceder al primer elemento
# print(names[-1]) # acceder al ultimo elemento
# del names[1] # eliminar el segundo elemento
# print(names)
# names.insert(1, "carlos") # insertar un elemento en la posicion 1
# print(names)
# print(names.count("carlos")) # contar cuantas veces aparece un elemento
# print(names.index("carlos")) # obtener el indice de un elemento
# names[3] = names[0] # cambiar el valor en la posicion 3
# names.append("ana") # agregar un elemento al final

#------Practica en clase-------

alumnos = ["nahomy", "habib", "jesus"]
alumnos.append("lucio") # agregar un elemento al final
alumnos.insert(1, "erik") # insertar un elemento en la posicion 1
alumnos.remove("habib") # eliminar un elemento por valor
alumnos.pop() # eliminar el ultimo elemento
print(alumnos) # ['nahomy', 'erik', 'jesus']

#recorrido de listas
for alumno in alumnos:
    print("Hola " + alumno)
    
    
nummeros = [10, 5, 7, 2, 1]
suma = 0

for numero in nummeros:
    suma += numero
print("La suma es: " + str(suma))