def contar_palabras_y_almacenar_en_matriz(nombre_archivo):
    """
    Cuenta la cantidad de palabras en un archivo de texto y las almacena en una matriz cuyo tamaño de sublistas
    se extrae de la fila 4 del archivo. La matriz se forma a partir de la línea 8 en adelante y excluye "EOF".

    :param nombre_archivo: Ruta del archivo de texto.
    :return: Una tupla con el número total de palabras y la matriz de palabras.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            # Extraer el tamaño de la sublista desde la fila 4
            tamano_sublista = int(lineas[3].split(":")[1].strip())
            
            # Obtener el contenido desde la línea 8 en adelante
            contenido = ''.join(lineas[7:])
            palabras = contenido.split()
            
            # Excluir "EOF" si está presente
            if palabras[-1] == "EOF":
                palabras = palabras[:-1]
            
            matriz = [palabras[i:i + tamano_sublista] for i in range(0, len(palabras), tamano_sublista)]
            return len(palabras), matriz
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return 0, []
    except (IndexError, ValueError):
        print("Error al leer el tamaño de la sublista desde la fila 4.")
        return 0, []

# Ejemplo de uso
if __name__ == "__main__":
    archivo = "br17.atsp"  # Cambia esto por el nombre de tu archivo
    total_palabras, matriz_palabras = contar_palabras_y_almacenar_en_matriz(archivo)
    print(f"El archivo contiene {total_palabras} palabras.")
    print("Matriz de palabras:")
    for sublista in matriz_palabras:
        print(sublista)