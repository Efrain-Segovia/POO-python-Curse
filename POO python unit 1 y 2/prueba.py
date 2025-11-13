class Pokemon:
    def __init__(self, nombre, nivel, hp, ataque, evolucion):
        self.nombre = nombre
        self.nivel = nivel
        self.hp = hp
        self.ataque = ataque
        self.evolucion = evolucion

    def mostrar_info(self):
        print(f"Soy {self.nombre}, nivel {self.nivel} con {self.hp} HP. Evolución: {self.evolucion}")

    def atacar(self):
        print(f"{self.nombre} usa {self.ataque}!")

mew = Pokemon("Mew", 100, 200, "Psíquico", True)





