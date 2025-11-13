class Pokemon():
  #Metodo constructor
  def __init__(self, nombre, tipo, nivel, hp, ataque):
    #Atributos de instancia
    self.nombre = nombre
    self.tipo = tipo
    self.nivel = nivel
    self.hp = hp
    self.ataque = ataque

  def mostrar_info(self):
    print(f"Mi nombre es: {self.nombre}")
    print(f"Soy de nivel: {self.nivel}")

pikachu = Pokemon("Pikachu", "Electrico", 5, 35, "Impactrueno")
charmander = Pokemon("Charmander", "Fuego", 5, 39, "Ascuas")

pikachu.mostrar_info()