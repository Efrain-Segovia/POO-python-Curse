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

# herencia jerárquica
class PokemonAgua(Pokemon):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Agua"
        self.debilidad = "Eléctrico"

    def atacar(self):
        print(f"{self.nombre} lanza un chorro de agua")


class PokemonPlanta(Pokemon):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Planta"
        self.debilidad = "Fuego"

    def atacar(self):
        print(f"{self.nombre} lanza hojas afiladas")


class PokemonFuego(Pokemon):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Fuego"
        self.debilidad = "Agua"

    def atacar(self):
        print(f"{self.nombre} lanza una llamarada")



# herencia múltiple
class PokemonAguaPlanta(PokemonAgua, PokemonPlanta):
    def __init__(self, nombre, nivel, hp, ataque):
        # Hereda el comportamiento de ambos padres
        super().__init__(nombre, nivel, hp, ataque) 
        self.tipo = "Agua/Planta"
        self.debilidad = "Fuego"  # predominante de Planta

    def atacar(self):
        print(f"{self.nombre} combina agua y hojas")


class PokemonPlantaFuego(PokemonPlanta, PokemonFuego):
    def __init__(self, nombre, nivel, hp, ataque):
        super().__init__(nombre, nivel, hp, ataque)
        self.tipo = "Planta/Fuego"
        self.debilidad = "Agua"  # predominante de Fuego

    def atacar(self):
        print(f"{self.nombre} lanza fuego con energía natural")


# usando el main para pruebas
if __name__ == "__main__":
    squirtle = PokemonAgua("Squirtle", 10, 35, "Burbuja")
    bulbasaur = PokemonPlanta("Bulbasaur", 10, 40, "Latigazo")
    charmander = PokemonFuego("Charmander", 10, 30, "Ascuas")
    ludicolo = PokemonAguaPlanta("Ludicolo", 35, 95, "Danza pétalo")
    cherrim = PokemonPlantaFuego("Cherrim", 28, 80, "Rayo solar")

    squirtle.mostrar_info()
    bulbasaur.mostrar_info()
    charmander.mostrar_info()
    ludicolo.mostrar_info()
    cherrim.mostrar_info()

    # for p in [squirtle, bulbasaur, charmander, ludicolo, cherrim]:
    #     p.mostrar_info()
    #     p.atacar()
    #     print(f"Tipo: {p.tipo} | Debilidad: {p.debilidad}")
    #     print("-" * 50)