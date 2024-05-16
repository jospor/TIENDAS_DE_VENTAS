from productos import Producto
from tienda import Supermercado

if __name__ == "__main__":
    mi_supermercado = Supermercado("Mi Supermercado", costo_delivery=3.0)

    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'salir' para finalizar): ")
        if nombre_producto.lower() == "salir":
            break

        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese el stock del producto: "))

        producto_nuevo = Producto(nombre_producto, precio_producto, stock_producto)
        mi_supermercado.ingresar_producto(producto_nuevo)

    print("\nProductos en Mi Supermercado:")
    print(mi_supermercado.listar_productos())

