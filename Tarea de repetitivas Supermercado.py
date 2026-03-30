Nombre = ""
PrecioFinal = 0
PrecioFinalSinDescuentos = 0
ProductosAComprar = 0
AhorroTotal = 0
promedio = 0
promedio2 = 0
respuesta = ""
while Nombre == "" or not Nombre.isalpha():
    Nombre = input("Ingresar nombre: ")
    if Nombre == "":
        print ("no es un nombre valido")
    if not Nombre.isalpha():
        print ("no se aceptan numeros")
while 0 >= ProductosAComprar:
    ProductosAComprar = (input("Cantidad de productos a comprar:"))
    if not ProductosAComprar.isdigit():
        print("eso no es un numero valido")
        ProductosAComprar = 0
    if 0 >= int(ProductosAComprar):
        print("tiene que ser mayor a 0")
        ProductosAComprar = 0
    else:
        ProductosAComprar = int(ProductosAComprar)
for x in range(1,ProductosAComprar + 1):
    y = int(input(f"Introducir precio del producto {x}: "))
    PrecioFinalSinDescuentos += y
    print("tiene este producto descuento?")
    while respuesta == "":
        respuesta = input("responder con (s/n): ")
        respuesta = respuesta.lower()
        if respuesta == "s":
            descuento = y * (10/100)
            y -= descuento
            AhorroTotal += descuento
            print(f"descuento aplicado, su precio ahora es del {y}")
            respuesta = ""
            break
        if respuesta == "n":
            respuesta = ""
            break
        else:
            print("intentelo de nuevo")
            respuesta = ""
    PrecioFinal += y
    promedio = PrecioFinalSinDescuentos/ProductosAComprar
    promedio2 = PrecioFinal/ProductosAComprar
print(f"precio final:{PrecioFinal}")
print(f"precio sin descuentos:{PrecioFinalSinDescuentos}")
print(f"ahorro total:{AhorroTotal}")
print(f"promedio de precio por producto sin descuentos: {promedio:.2f}")
print(f"promedio de precio por producto con descuentos: {promedio2:.2f}")