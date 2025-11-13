class Pokemon_0():
  #Atributos estaticos
  nombre = "pikachu"
  tipo = "electrico"
  nivel = 5
  hp = 35
  ataque = "impactrueno"

#Crear un objeto de la clase Pokemon_0
pikachu_0 = Pokemon_0()

print(pikachu_0.nombre)  # Output: pikachu
pikachu_0.nombre = "Raichu"
print(pikachu_0.nombre)  # Output: Raichu

class Pokemon():
  #Metodo constructor
  def __init__(self, nombre, tipo, nivel, hp, ataque):
    #Atributos de instancia
    self.nombre = nombre
    self.tipo = tipo
    self.nivel = nivel
    self.hp = hp
    self.ataque = ataque

pikachu = Pokemon("Pikachu", "Electrico", 5, 35, "Impactrueno")
charmander = Pokemon("Charmander", "Fuego", 5, 39, "Ascuas")

print(pikachu.nombre)  # Output: Pikachu
print(pikachu.tipo)    # Output: Electrico

print(charmander.nombre)  # Output: Charmander
print(charmander.tipo)    # Output: Fuego


if __name__ == "__main__":
    bulbasaur = Pokemon("Bulbasaur", "Planta", 5, 45, "Latigazo")
    print(bulbasaur.nombre)  # Output: Bulbasaur
    print(bulbasaur.tipo)    # Output: Planta
