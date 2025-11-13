# Cual es el valor que recibira x
x = 5
x = x == x
print(x)

#Cuantos * Se veran en pantalla
i = 0
while i <= 3 :
    i += 2
    print("*")


#Cuantos * Se veran en pantalla
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

#Cuantos # Se veran en pantalla
for i in range(1):
    print("#")
else:
    print("#")

# ...
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

# Output
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)

