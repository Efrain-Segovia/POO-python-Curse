#Alcances

#Sin Alcance, alcance local
# x = 2
# print(x)

# def scope_test():
#     global x
#     x = 123

# print(x)

# Alcance local
# def func_local():
#     global var_local
#     var_local = "Soy una variable local"
#     print(var_local)
# func_local()
# print(var_local)

# #Alcance global
# var_global = "Soy una variable global"
# def func_global():
#     print(var_global)
# func_global()
# print(var_global)

#Modificacion de variables globales
contador = 0
def incrementar():
    global contador
    contador += 1
incrementar()
incrementar()
print(contador)