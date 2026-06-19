from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    
   
  @abstractmethod
  def describe(self):
      pass

class Cashier(User): 
  def __init__(self,dni:str,name:str,age:int,timeTable:str,salary:float):
    # Empleamos el método super() para heredar de user los parámetros de la Class superior en este caso, User.
    # Esta comparte atributos con esta (Cashier) y customer, si bien cada función concreta dentro de la class son diferentes
    # aunque sea describe, cada una lo hace de una manera concreta, y no sería compatible ya que no recibe los mismos datos o petaría
    # por cuestión de tipo de variable definida vs recibido en CSV.
    super().__init__(dni, name, age)
    self.timeTable = timeTable
    self.salary = salary
 
  def describe(self):
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."

class Customer(User):
  # Empleamos super() para llamar al constructor de la clase padre User, al igual que antes, el comentario aplica ambos.
  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
    super().__init__(dni, name, age)
    self.email = email
    self.postalCode = postalCode

  def describe(self):
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"