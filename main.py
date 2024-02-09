from decimal_binario import *
from binario_decimal import *
from string_base64 import *

def main():
    cadena = "Sun"

    # Obteniendo los valores ASCII de los caracteres
    ascii_resultado = caracteres_a_ascii(cadena)
    print("Representación ASCII de la cadena:")
    print(ascii_resultado)

    # Convertiendo los valores ASCII a su representación binaria manualmente
    binario_resultado = [ascii_a_binario_manual(valor) for valor in ascii_resultado]
    print("Representación binaria de la cadena:")
    print(binario_resultado)
    
    base64 = bin_to_base64(binario_resultado)
    print("Representación base 64 de la cadena:")
    print(base64)

    # # Convertiendo la representación binaria a la cadena original
    # cadena_original = binario_a_cadena(''.join(binario_resultado))
    # print("Cadena original obtenida de la representación binaria:")
    # print(cadena_original)

if __name__ == "__main__":
    main()