# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


# Herencia directa
class Entrenador(Persona):
    def __init__(self, nombre, edad, medallas):
        super().__init__(nombre, edad)
        self.medallas = medallas

    def mostrar_info(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y {self.medallas} medallas.")

    def atacar(self):
        print(f"{self.nombre}: ¡Te reto a una batalla Pokémon!")


# Herencia directa
class NPC(Persona):
    def __init__(self, nombre, edad, oficio):
        super().__init__(nombre, edad)
        self.oficio = oficio

    def mostrar_info(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y trabajo como {self.oficio}.")

    def hablar(self):
        print(f"{self.nombre}: ¡Hola viajero, bienvenido a la ciudad!")


# Herencia directa (de Persona)
class Investigador(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"Soy el profesor {self.nombre}, tengo {self.edad} años y estudio los Pokémon tipo {self.especialidad}.")

    def hablar(self):
        print(f"{self.nombre}: Los Pokémon de tipo {self.especialidad} son fascinantes.")


# Herencia múltiple (NPC + Entrenador)
class Ofensivo(NPC, Entrenador):
    def __init__(self, nombre, edad, oficio, medallas):
        # Llamamos directamente a Persona para evitar conflictos con super()
        # Persona es la clase común en la jerarquía
        Persona.__init__(self, nombre, edad)
        self.oficio = oficio
        self.medallas = medallas

    def mostrar_info(self):
        print(f"Soy {self.nombre}, {self.oficio} con {self.medallas} medallas. ¡Estoy listo para pelear!")

    def atacar(self):
        print(f"{self.nombre}: ¡Prepárate, te desafiaré a una batalla Pokémon!")


# Herencia jerárquica (subclase de NPC)
class Inofensivo(NPC):
    def __init__(self, nombre, edad, oficio):
        super().__init__(nombre, edad, oficio)

    def mostrar_info(self):
        print(f"Soy {self.nombre}, un {self.oficio} pacífico, no peleo con nadie.")

    def hablar(self):
        print(f"{self.nombre}: ¡Qué buen día para entrenar Pokémon!")


# Pruebas
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