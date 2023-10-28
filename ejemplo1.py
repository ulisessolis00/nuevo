#Realiza un programa que calcule el iva de un producto, dado su precio

print("A continuacion vamos a calcular el iva del precio que tu ingreses")

precio = float(input("Ingresa el precio del articulo: \n"))

iva = precio * 0.16

print(f"El precio del articulo es {precio} y el iva es {iva}, asi que por lo tanto, el costo total del producto es {precio+iva}")