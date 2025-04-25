def contar_palabras_y_almacenar_en_matriz(nombre_archivo):
    """
    Cuenta la cantidad de palabras en un archivo de texto y las almacena en una matriz de tamaño n.

    :param nombre_archivo: Ruta del archivo de texto.
    :param n: Tamaño de las sublistas en la matriz.
    :return: Una tupla con el número total de palabras y la matriz de palabras.
    """
    try:
        with open("br17.atsp", 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            # Extraer el tamaño de la sublista desde la fila 4
            n = int(lineas[3].split(":")[1].strip())

            contenido = archivo.read()
            palabras = contenido.split()
            matriz = [palabras[i:i + n] for i in range(0, len(palabras), n)]
            return len(palabras), matriz
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return 0, []

# Ejemplo de uso
if __name__ == "__main__":
    archivo = "br17.atsp"  # Cambia esto por el nombre de tu archivo
    #tamano_sublista = 17  # Cambia esto por el tamaño deseado de las sublistas
    total_palabras, matriz_palabras = contar_palabras_y_almacenar_en_matriz(archivo)
    print(f"El archivo contiene {total_palabras} palabras.")
    print("Matriz de palabras:")
    for sublista in matriz_palabras:
        print(sublista)