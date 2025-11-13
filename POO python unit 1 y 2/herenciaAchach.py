from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def comer(self):
    pass

  @abstractmethod
  def dormir(self):
    pass

class avestrus(Animal):
  def comer(self):
    return "come plantas y animales peques"
  
  def dormir(self):
    return "duerme acostado"
  
guajolote = avestrus()
