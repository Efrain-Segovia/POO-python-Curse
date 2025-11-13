# Implementación recursiva de la función factorial.

# def factorial(n):
#     if n == 1:    # El caso base (condición de terminación).
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(8)) # 4 * 3 * 2 * 1 = 24

# Implementación recursiva de la función para calcular la suma de los primeros n números naturales.
# def sum_natural_numbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_natural_numbers(n - 1)

# print(sum_natural_numbers(5)) # 5 + 4 + 3 + 2 + 1 = 15

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))

