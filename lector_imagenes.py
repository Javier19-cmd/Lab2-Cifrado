def leer_imagen(ruta):
    try:
        with open(ruta, 'rb') as f:
            contenido = f.read()
        return ['{:08b}'.format(byte) for byte in contenido]
    except IOError:
        print("El archivo no se pudo abrir. Puede estar corrupto o el archivo puede no existir.")

ruta_imagen = "imagen_xor.png"
contenido_imagen = leer_imagen(ruta_imagen)

print(contenido_imagen)