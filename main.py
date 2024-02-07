from decimal_binario import *
from binario_decimal import *

cadena = "Hola"

# Obteniendo los valores ASCII de los caracteres
ascii_resultado = caracteres_a_ascii(cadena)
print("Representación ASCII de la cadena:")
print(ascii_resultado)

# Convertir los valores ASCII a su representación binaria manualmente
binario_resultado = [ascii_a_binario_manual(valor) for valor in ascii_resultado]
print("Representación binaria de la cadena:")
print(binario_resultado)

# Convertir representación binaria a la cadena original
cadena_original = binario_a_cadena(''.join(binario_resultado))
print("Cadena original obtenida de la representación binaria:")
print(cadena_original)