"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
from util import *
from users import *
from products import *
from orders import *
## añadimos esto para la extensión necesaria para el write
from datetime import datetime
import pandas as pd

class PrepareOrder:
    def __init__(self):
        cashiers = CSVFileManager("data/cashiers.csv").read()
        self.cashiers = CashierConverter().convert(cashiers)
        #CashierConverter().print(self.cashiers)  
        '''
        --> me aprecía más óptimo no mostrar la lista entera , esta y las siguientes, ya que al hacer la carga así
        te salia un mega listado y encontrar el tema era como complicado, en cambio, haciendo un show controlado, 
        a medida que pide inputs, te las visualiza de manera controlada garantizando mayor accesibilidad al usuario
        '''
              
        customers = CSVFileManager("data/customers.csv").read()
        self.customers = CustomerConverter().convert(customers)
        #CustomerConverter().print(self.customers) 

        drinks = CSVFileManager("data/drinks.csv").read()
        self.drinks = ProductConverter().convert(drinks,Drink)
        #ProductConverter().print(self.drinks) 
      
        hamburgers = CSVFileManager("data/hamburgers.csv").read()
        self.hamburgers = ProductConverter().convert(hamburgers,Hamburger)
        #ProductConverter().print(self.hamburgers) 
        
        happyMeal = CSVFileManager("data/happyMeal.csv").read()
        self.happyMeal = ProductConverter().convert(happyMeal, HappyMeal)
        #ProductConverter().print(self.happyMeal) 
        
        sodas = CSVFileManager("data/sodas.csv").read()
        self.sodas = ProductConverter().convert(sodas, Soda)
        #ProductConverter().print(self.sodas) 
                           
    def find_cashier(self, dni):
        # método definido como bucle que recorrelos cashiers previamente generados (self.cashiers) para encontrar
        # el que haga match con el dni que viene entrado  en un momento, en este caso vía input
        for cashier in self.cashiers:
            if cashier.dni == dni:
                return cashier
        return None
    
    def find_customer(self, dni):
        # lo mismo que el anterior pero para customers
        for customer in self.customers:
            if customer.dni == dni:
                return customer
        return None


    def find_products(self, id):
        # igual que el anterior, lo único que no tendría sentido hacer un find_products por tipo, facilita hacer uniones para hacer lectura
        # completa, si bien hay un tema, y es que si existe el ID pasado, validará de manera total que existe, no hago ningún juego
        # que permita meter un producttype o algo así para hacer un find_products inteligente en base a la clase que tocamos, se podría haber
        # valorado        
        listacompleta = self.hamburgers + self.sodas + self.drinks + self.happyMeal
        for product in listacompleta:
            if product.id == id:
                return product
        return None    
    
    def show_customers(self):
        print("Customers list:")
        CustomerConverter().print(self.customers)
        
    def show_cashiers(self):
        print("Cashiers list:") # --> Corregido tipo vs carga previa
        CashierConverter().print(self.cashiers) 

    def show_products(self, *args):
        # es la misma rutina que otros shows pero se pasa variable para inputar directamente la variable que determinará que listado
        # mostrará, si bien protegido vía diccionario
        productos = {"Hamburgers": self.hamburgers
                     , "Sodas": self.sodas
                     , "Drinks": self.drinks
                     , "HappyMeal": self.happyMeal
                     }
        if args[0] not in productos:
            print(f"Tipo de producto no válido: {args[0]}\nIntroduce: Hamburgers, Sodas, Drinks o HappyMeal")
            return None
        print("Product list:")
        ProductConverter().print(productos[args[0]])
        return True
      
    ## genero método adicional para facilitar el programa final la elección del artículo
    def escoger_producto(self, producttype ,order):
        producto = input("Introduce id del producto deseado (ej: G1, H1): ")
        product = self.find_products(producto)
        while product is None:
            self.show_products(producttype)            
            producto = input("Introduce el id del producto (o 'exit' para salir): ")
            if producto == 'exit':     
                return       
            product = self.find_products(producto)
            if product is None:
                print("Producto no encontrado, inténtalo de nuevo")
        order.add(product)
        
    ## genero método adicional para facilitar el programa final de visualización del tipo de pedido
    ## de hecho, me permite invocar el tipo y añadir el bucle de pedir más o l oque sea, de manera que puedo jugar después
    ## a meter este o el simple para mantener misma categoría
    def escoger_tipo(self, order):
        producttype = input("Elige productos de entre la siguiente lista: Hamburgers, Sodas, Drinks o HappyMeal:")
        resultado  = self.show_products(producttype)
        while resultado is None:
            producttype = input("Introduce tipo de producto (o 'exit' para salir): ")
            if producttype == 'exit':
                return  # Lo mismo, fuerza salida si no es capaz de dar con el tipo o quiere cerrar
            resultado = self.show_products(producttype)
            if resultado is None:
                print("Listado no encontrado, inténtalo de nuevo")
        self.escoger_producto(producttype, order)
        return producttype
       
    def generar(self):
        # vamos primero a introducir, y proteger, el cashier
        cashier = None
        while cashier is None:
            self.show_cashiers()
            dni = input("Introduce DNI del cajero (o 'exit' para salir): ")
            if dni == 'exit':
                return  # si por lo que sea no le sale el DNI pretendido, podría querer salir del método y revisar bbdd por ejemplo
            cashier = self.find_cashier(dni)
            if cashier is None:
                print("Cajero no encontrado, inténtalo de nuevo.")
        print(cashier.describe())
        
        ## ahora vamos con el customer
        customer = None
        while customer is None:
            self.show_customers()
            dni = input("Introduce DNI del cliente (o 'exit' para salir): ")
            if dni == 'exit':
                return  # si por lo que sea no le sale el DNI pretendido,
                        # quien genera el pedido podría querer salir del método activo
                        # y revisar bbdd por ejemplo
            customer = self.find_customer(dni)
            if customer is None:
                print("Cliente no encontrado, inténtalo de nuevo.")
        print(customer.describe())  

        # toca generar order, le pasamos cajero y cliente como paramétros ya comprobados previos
        order = Order(cashier, customer)

        # toca añadir los productos, aquí haremos bucles para que el generador tenga en cuenta 
        # juego de cambios de clases de productos y de esta manera mostrar a medida que lo requiera 
        # el listado de productos previamente tratado
        # para hacerlo, se han generado funciones adicionales de apoyo. Simplifica lenguaje
        producttype = self.escoger_tipo(order)
        if producttype is None:
            return 
        # metemos protección a si o no, ya que incialmente lo hice con si pero vi que si ponía otra cosa interpretaba que era no
        # que es lo mismo, pero no elegante. Releyendo el código me planteo hacer función adicional para evitar repetir código.
        otro = None
        while otro not in ["si", "no"]:
            otro = input("¿Quieres añadir otro producto? (Si/No): ").lower()
            if otro not in ["si", "no"]:
                print("Por favor introduce Si o No")
                
        # y empieza el juego
        while otro.lower() == "si":
            visualiza = None
            while visualiza not in ["si", "no"]:
                visualiza = input("¿Cambiar categoría? (Si/No): ").lower()
                if visualiza not in ["si", "no"]:
                    print("Por favor introduce Si o No")
            if visualiza.lower() == 'si':
                producttype = self.escoger_tipo(order)
            else:
                self.escoger_producto(producttype, order)
            otro = None
            while otro not in ["si", "no"]:
                otro = input("¿Quieres añadir otro producto? (Si/No): ").lower()
                if otro not in ["si", "no"]:
                    print("Por favor introduce Si o No")        
    
        # mostramos el orden generado, ya está hecho!    
        order.show()
        
        # Registramos y generamos en un dataframe los datos según enunciados que pasaremos al objeto de write definidos en file_manager
        df_ventas = pd.DataFrame({
            'dni_cajero': [order.cashier.dni],
            'dni_comprador': [order.customer.dni],
            'fecha_venta': [datetime.now()],
            'total': [order.calculateTotal()]
        })
        path = "data/orders.csv"
        CSVFileManager(path).write(df_ventas)

# llamada a la función principal que invoca el proceso          
PrepareOrder().generar()
