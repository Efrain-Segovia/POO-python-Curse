#comunicacion entre funciones

#Funciones parametrizadas
# def saludar(nombre):
#     print("Hola", nombre)

# saludar("Ana")

#sombreado de variables
#variable con el mismo nombre del parámetro de la función.

# def mostrar_variable():
#     var_local = "Soy una variable local"
#     print(var_local)

# mostrar_variable()
# var_local = "Soy una variable global"
# print(var_local)

#Funciones invocadas con su parametro
# def sumar(a, b):
#     return a + b

# suma = sumar(3, 5)
# print(suma)
# sumar(a=3, b=5)
# sumar(x=3, y=5)



def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# adding(1, 2, 3)
# adding(c=3, a=1, b=2)
adding(2, c=3, b=1)
# adding(b=2, c=3, a=1)
#no hacerlo asi:
# adding(b=3, 1, c=2) #Error
# adding(b=1, 2, c=3) #Error
# adding(1, 2, c=3) #Correcto

#parametros por defecto
def potencia(base=1, exponente=2):
    print(base ** exponente)

potencia()
potencia(3)
potencia(3, 3)
potencia(3,base=)
