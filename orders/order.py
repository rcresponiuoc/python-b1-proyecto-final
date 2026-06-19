from users import *
from products import *

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
      self.products.append(product)# añade a la lista definida en Order.products los valores del product que vienen

  def calculateTotal(self) -> float: # función incremental, se define variable a 0 y un bucle que incrementará segun se definan productos
        total = 0
        for product in self.products:
            total = total + product.price
        return total
  
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {round(self.calculateTotal(),2)}")## v2. se hace round, en un order concreto me salieron muchos decimales
