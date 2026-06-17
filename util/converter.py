from abc import ABC, abstractmethod
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