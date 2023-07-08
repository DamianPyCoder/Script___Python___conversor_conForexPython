from forex_python.converter import CurrencyRates

def convertir_divisas(cantidad, moneda_origen, moneda_destino):
    c = CurrencyRates()
    resultado = c.convert(moneda_origen, moneda_destino, cantidad)
    return resultado

# Obtén los detalles de las monedas de origen y destino
moneda_origen = input("Introduce la moneda de origen: ")
moneda_destino = input("Introduce la moneda de destino: ")
cantidad = float(input("Introduce la cantidad a convertir: "))

# Convierte las monedas
resultado = convertir_divisas(cantidad, moneda_origen, moneda_destino)
print(f"{cantidad} {moneda_origen} equivale a {resultado} {moneda_destino}")
