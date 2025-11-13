#listas y funciones

#len()
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

numbers = [1, 2, 3, 4, 5]
result = list_sum(numbers)
print("La suma de", numbers, "es", result)

def list_average(lst):
    total = list_sum(lst)
    count = len(lst)
    average = total / count
    return average #retorna el promedio

average_result = list_average(numbers)
print("El promedio de", numbers, "es", average_result)

#numeros pares en una lista
def filter_even_numbers(lst):
    even_numbers = []

    for elem in lst:
        if elem % 2 == 0:
            even_numbers.append(elem)

    return even_numbers #retorna una nueva lista
even_numbers_result = filter_even_numbers(numbers)
print("Los números pares en", numbers, "son", even_numbers_result)