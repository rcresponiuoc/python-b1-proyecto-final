from abc import ABC, abstractmethod
## importamos los products y users para que estos objetos puedan ser capaces de localizar el resto de clases/ metodos
## y emplearlos cuando se necesario.
from products import *
from users import *

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):
    cashiers = []
    '''
    tras tratar de averiguar cual era la mejor opción, iterrows del paquete pandas es la escogida
    El tema es aplicar _ para omitir el indice en el bucle, de lo contrario no podría pasar el parametro obtenido por nombre de columna
    sino que tendría que ir por posición en el row[posición] cuyo valor quiero pasarle contra DNI y demás.
    '''
    for _, row in dataFrame.iterrows():
      cashier = Cashier(
          dni=str(row['dni']),
          name=row['name'],
          age=row['age'],
          timeTable=row['timetable'],
          salary=row['salary']
      )
      cashiers.append(cashier)
    return cashiers

class CustomerConverter(Converter):
  def convert(self,dataFrame):    
    customers = []
    # Aplica la misma logica que el anterior
    for _, row in dataFrame.iterrows():
      customer = Customer(
          dni=str(row['dni']),
          name=row['name'],
          age=row['age'],
          email=row['email'],
          postalCode=row['postalcode']
      )
      customers.append(customer)
    return customers
  
class ProductConverter(Converter):
  # A diferencia del anterior, en este caso se debe definir un argumento adicional que en este caso,
  # permitirá simplificar el programa. Lo "único cosmético", es la definición de product_class para hacer más legible el código 
  # podría dirigir args[0] en el cicle sin problema en la definición concreta de product previo append.
  # se mete, un valor de excepción en Value error, por si llega un input no controlado en valid_classes
  def convert(self,dataFrame , *args):    
    products = []
    product_class = args[0]
    valid_classes = [Hamburger, Soda, Drink, HappyMeal]
    if args[0] not in valid_classes:
      raise ValueError(f"Tipo de producto no válido: {args[0]}")
    for _, row in dataFrame.iterrows():
      product = product_class(
        id=str(row['id']),
        name=row['name'],
        price=row['price']
        )
      products.append(product)
    return products