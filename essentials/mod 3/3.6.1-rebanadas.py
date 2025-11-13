#rebanadas
names = ["ana", "beto", "cata", "dani", "eva", "fito", "gala"]
print(names[2:5]) # desde el indice 2 hasta el 4
print(names[:4]) # desde el inicio hasta el indice 3
print(names[3:]) # desde el indice 3 hasta el final
print(names[:]) # toda la lista
print(names[1:6:2]) # desde el indice 1 hasta el 5 de 2 en 2
print(names[::-1]) # lista invertida
print(names[-5:-2]) # desde el indice -5 hasta el -3

del names[2:4] # eliminar elementos desde el indice 2 hasta el 3
print(names)
names[1:3] = ["carlos", "daniela"] # cambiar elementos desde el indice 1 hasta el 2
print(names)

# in y not in
numbers = [1, 3, 5, 7, 9]
print(3 in numbers) # True
print(4 in numbers) # False
print(4 not in numbers) # True
print(5 not in numbers) # False



# my_list = [8, 10, 6, 2, 4]  
# my_list2 = my_list[:]

# del my_list[-1]

# print(my_list)

# print(my_list2)