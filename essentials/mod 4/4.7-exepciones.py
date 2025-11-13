#excepciones

#errores con datos
# a = "10"
# b = 2
# # print(a + b)  # TypeError: no se pueden sumar str y int

# try:
#     print(a + b)
# except TypeError:
#     print("Error: No se pueden sumar str y int")
#     print("Convirtiendo 'a' a int...")
#     a = int(a)
#     print("Ahora la suma es:", a + b)

# x = 1
# y = 0
# try:
#     print(x/y)
# except ZeroDivisionError:
#     print("no se puede dividir entre cero")
# except:
#     print("algo salio")


#manejo de division entre cero
# numerador = 10
# denominador = 0
# try:
#     resultado = numerador / denominador
#     print("El resultado es:", resultado)
# except ZeroDivisionError:
#     print("Error: División entre cero no permitida.")
#     denominador = 1  # Asignar un valor diferente a cero
#     resultado = numerador / denominador
#     print("Nuevo resultado con denominador 1:", resultado)

# #manejo de llaves en diccionarios
# mi_diccionario = {"nombre": "Ana", "edad": 25}
# try:
#     print("La ciudad es:", mi_diccionario["ciudad"])
# except KeyError:
#     print("Error: La clave 'ciudad' no existe en el diccionario.")
#     mi_diccionario["ciudad"] = "Desconocida"  # Agregar la clave con un valor por defecto
#     print("Ciudad agregada con valor por defecto:", mi_diccionario["ciudad"])
    
# # multiples excepciones
# valores = [10, 0, "cinco", 20]
# for valor in valores:
#     try:
#         resultado = 100 / valor
#         print(f"100 dividido por {valor} es {resultado}")
#     except ZeroDivisionError:
#         print("Error: División entre cero no permitida.")
#     except TypeError:
#         print(f"Error: No se puede dividir por un valor de tipo {type(valor).__name__}.")
        
# # finally
# try:
#     archivo = open("archivo_inexistente.txt", "r")
#     contenido = archivo.read()
#     print(contenido)
# except FileNotFoundError:
#     print("Error: El archivo no existe.")
# finally:
#     print("Operación de manejo de archivos finalizada.")        
    
# # 
# while True:
#     try:
#         number = int(input("Ingresa un número entero: "))
#         print(5/number)
#         break
#     except (ValueError, ZeroDivisionError, SyntaxError):
#         print("Valor incorrecto o se ha roto la regla de división entre cero.")
#         number = 1
#     except:
#         print("Lo siento, algo salió mal...")

# x = 3
# print(len(x))
try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")

