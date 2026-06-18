from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
    ### en el enunciado en lugar de "empaque" usan "Wrapping" pero dado que viene por defecto así, lo dejamos.
    # Quizá se debería hacer en inglés
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return 'Aluminium'

## Se define el pack y material en base al ejemplo (pagina 7)
class Bottle(FoodPackage):  
  def pack(self):
    return "Bottle"
  def material(self):
    return 'Plastic'

# Definido glass siguiendo ejemplo página 1, en inglés
class Glass(FoodPackage):  
  def pack(self):
    return "Glass"
  def material(self):
    return 'Cardboard'

# el primero comentado, el segundo por intuición que sea caja de cartón?
class Box(FoodPackage):  
  def pack(self):
    return "Box"
  def material(self):
    return 'Cardboard'