from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Papel"
  def material(self):
    return 'Aluminium'

class Bottle(FoodPackage):  
  #Write your code here
  pass
      
class Glass(FoodPackage):  
  #Write your code here
  pass

class Box(FoodPackage):  
  #Write your code here
  pass