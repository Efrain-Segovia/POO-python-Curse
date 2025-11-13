# Clase base
class Persona:
    def __init__(self, nombre, edad, **kwargs):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


# Herencia directa
class Entrenador(Persona):
    def __init__(self, nombre, edad, medallas=0, **kwargs):
        super().__init__(nombre, edad, **kwargs)
        self.medallas = medallas

    def mostrar_info(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y {self.medallas} medallas.")

    def atacar(self):
        print(f"{self.nombre}: ¡Te reto a una batalla Pokémon!")


# Herencia directa
class NPC(Persona):
    def __init__(self, nombre, edad, oficio="Civil", **kwargs):
        super().__init__(nombre, edad, **kwargs)
        self.oficio = oficio

    def mostrar_info(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y trabajo como {self.oficio}.")

    def hablar(self):
        print(f"{self.nombre}: ¡Hola viajero, bienvenido a la ciudad!")


# Herencia directa
class Investigador(Persona):
    def __init__(self, nombre, edad, especialidad="Pokémon", **kwargs):
        super().__init__(nombre, edad, **kwargs)
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"Soy el profesor {self.nombre}, tengo {self.edad} años y estudio los Pokémon tipo {self.especialidad}.")

    def hablar(self):
        print(f"{self.nombre}: Los Pokémon de tipo {self.especialidad} son fascinantes.")


# Herencia múltiple (NPC + Entrenador)
class Ofensivo(NPC, Entrenador):
    def __init__(self, nombre, edad, oficio, medallas, **kwargs):
        super().__init__(nombre=nombre, edad=edad, oficio=oficio, medallas=medallas, **kwargs)

    def mostrar_info(self):
        print(f"Soy {self.nombre}, {self.oficio} con {self.medallas} medallas. ¡Estoy listo para pelear!")

    def atacar(self):
        print(f"{self.nombre}: ¡Prepárate, te desafiaré a una batalla Pokémon!")


# Herencia jerárquica (subclase de NPC)
class Inofensivo(NPC):
    def __init__(self, nombre, edad, oficio="Ciudadano", **kwargs):
        super().__init__(nombre=nombre, edad=edad, oficio=oficio, **kwargs)

    def mostrar_info(self):
        print(f"Soy {self.nombre}, un {self.oficio} pacífico, no peleo con nadie.")

    def hablar(self):
        print(f"{self.nombre}: ¡Qué buen día para entrenar Pokémon!")


ash = Entrenador("Ash", 10, 8)
ash.mostrar_info()
ash.atacar()
print()

juan = NPC("Juan", 25, "Vendedor")
juan.mostrar_info()
juan.hablar()
print()

oak = Investigador("Oak", 50, "Planta")
oak.mostrar_info()
oak.hablar()
print()

brock = Ofensivo("Brock", 18, "Líder de Gimnasio", 5)
brock.mostrar_info()
brock.atacar()
print()

maya = Inofensivo("Maya", 22, "Ciudadana")
maya.mostrar_info()
maya.hablar()
