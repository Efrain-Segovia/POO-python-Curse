class Pokemon:
    def __init__(self, nombre, nivel, hp, ataque):
        self.nombre = nombre
        self.nivel = nivel
        self.hp = hp
        self.ataque = ataque

    def mostrar_info(self):
        print(f"Soy {self.nombre}, nivel {self.nivel} con {self.hp} HP.")

    def atacar(self):
        print(f"{self.nombre} usa {self.ataque}!")


class PokemonAgua(Pokemon):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Agua"
        self.debilidad = "Eléctrico"

    def atacar(self):
        print(f"{self.nombre} lanza un chorro de agua")


class PokemonFuego(Pokemon):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Fuego"
        self.debilidad = "Agua"

    def atacar(self):
        print(f"{self.nombre} lanza una llamarada")


class PokemonPlanta(Pokemon):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Planta"
        self.debilidad = "Fuego"

    def atacar(self):
        print(f"{self.nombre} lanza hojas afiladas")