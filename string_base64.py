def bin_to_base64(bin_list):
    # Convertir de binario a ASCII
    ascii_list = [chr(int(b, 2)) for b in bin_list]
    ascii_string = ''.join(ascii_list)

    # Convertir de ASCII a base 64 de manera manual
    base64_string = ''
    base64_chars = {i: char for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

    # Convertir cada caracter a su representación binaria de 8 bits
    bin_string = ''.join([format(ord(c), '08b') for c in ascii_string])

    # Añadir ceros al principio si la longitud no es múltiplo de 6
    while len(bin_string) % 6 != 0:
        bin_string = '0' + bin_string

    # Convertir cada grupo de 6 bits a su correspondiente caracter en base 64
    for i in range(0, len(bin_string), 6):
        base64_string += base64_chars[int(bin_string[i:i+6], 2)]

    # Añadir '=' al final si la longitud no es múltiplo de 4
    while len(base64_string) % 4 != 0:
        base64_string += '='

    return base64_string