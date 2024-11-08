# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms
usuario=float(input("Por favor ingrese la medida de la pieza en cm: "))

# Paso 2: Convertir las medidas de centímetros a pulgadas
conversion=usuario/2.54
valor_redondeado=round(conversion,2)

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario 
mostrar= print(f'La medida de la pieza  es: {valor_redondeado} plg')