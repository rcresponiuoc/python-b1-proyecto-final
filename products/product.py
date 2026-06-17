from abc import ABC, abstractmethod
from .food_package import *

class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass  

# empleando Self para dotar de identidad propia bajo los atributos que correspodan, al objeto (productos)
# que obtendremos una vez pasados los parametros, en este caso, siguiedno los ejemplos/ datas
class Hamburger(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Soda"
    def foodPackage(self) -> FoodPackage:
        return Bottle()

class Drink(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Drink"
    def foodPackage(self) -> FoodPackage:
        return Glass()

class HappyMeal(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "HappyMeal"
    def foodPackage(self) -> FoodPackage:
        return Box()