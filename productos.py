
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)  # No permitir stock negativo

    def __str__(self):
        return f"{self.__nombre} - Precio: ${self.__precio:.2f} - Stock: {self.__stock}"

    def __eq__(self, other):
        return self.__nombre == other.__nombre

    def __add__(self, other):
        return Producto(self.__nombre, self.__precio, self.__stock + other.__stock)

    def __sub__(self, other):
        return Producto(self.__nombre, self.__precio, self.__stock - other.__stock)

    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock
 