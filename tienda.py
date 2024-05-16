
from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre: str, costo_delivery: float):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        if producto not in self.__productos:
            self.__productos.append(producto)
        else:
            existing_product = self.__productos[self.__productos.index(producto)]
            existing_product += producto

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, producto, cantidad):
        pass

    def obtener_nombre(self):
        return self.__nombre

    def obtener_costo_delivery(self):
        return self.__costo_delivery

class Restaurante(Tienda):
    def listar_productos(self):
        return "\n".join(str(p) for p in self.__productos)

    def realizar_venta(self, producto, cantidad):
        pass

class Supermercado(Tienda):
    def listar_productos(self):
        return "\n".join(str(p) for p in self.__productos)

    def realizar_venta(self, producto, cantidad):
        pass

class Farmacia(Tienda):
    def listar_productos(self):
        return "\n".join(p.obtener_nombre() for p in self.__productos)

    def realizar_venta(self, producto, cantidad):
        pass
