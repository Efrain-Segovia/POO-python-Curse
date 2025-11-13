#return en funciones

#return sin nada: None
def nada():
  return 
print(nada())
print(type(None))
x = None
y = nada()
#caracteristicas del None
# - Es un tipo de dato
# - Es el valor de retorno por defecto de una función
# - Se puede asignar a una variable
# - Se puede usar en comparaciones
# var = nada()
# print(type(var))

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")

happy_new_year(False)

